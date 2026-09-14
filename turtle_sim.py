import sys
import tty
import termios
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class WasdTeleop(Node):

    def __init__(self):
        super().__init__('wasd_teleop_node')
        # Publisher to the standard turtlesim movement topic
        self.publisher_ = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)
        
        # Configure movement speeds
        self.linear_speed = 2.0   # Speed for W and S
        self.angular_speed = 2.0  # Turning speed for A and D
        
        # Keep track of terminal settings to read raw keystrokes
        self.settings = termios.tcgetattr(sys.stdin)
        
        # Print control instructions to the user
        self.print_instructions()

    def print_instructions(self):
        self.get_logger().info("\n"
                               "-----------------------------\n"
                               "Control Your Turtle with WASD\n"
                               "-----------------------------\n"
                               "W : Forward  |  S : Backward\n"
                               "A : Left     |  D : Right\n"
                               "Q : Quit Program\n"
                               "-----------------------------")

    def get_key(self):
        """Reads a single keypress from the terminal without needing Enter."""
        tty.setraw(sys.stdin.fileno())
        key = sys.stdin.read(1)
        # FIX HERE: Changed sys.fileno() to sys.stdin.fileno() and kept 3 arguments
        termios.tcsetattr(sys.stdin.fileno(), termios.TCSADRAIN, self.settings)
        return key

    def run(self):
        """Main loop that waits for keys and publishes velocity messages."""
        twist = Twist()
        
        try:
            while True:
                key = self.get_key().lower()
                
                # Reset velocities every loop iteration
                twist.linear.x = 0.0
                twist.angular.z = 0.0

                if key == 'w':
                    twist.linear.x = self.linear_speed
                elif key == 's':
                    twist.linear.x = -self.linear_speed
                elif key == 'a':
                    twist.angular.z = self.angular_speed
                elif key == 'd':
                    twist.angular.z = -self.angular_speed
                elif key == 'q':
                    self.get_logger().info("Quitting WASD Teleop...")
                    break
                else:
                    # Ignore any other keys
                    continue

                # Send the movement command to TurtleSim
                self.publisher_.publish(twist)
                
        except Exception as e:
            self.get_logger().error(f"Error encountered: {e}")
        finally:
            # Always ensure the turtle stops moving when exiting
            twist.linear.x = 0.0
            twist.angular.z = 0.0
            self.publisher_.publish(twist)
            # FIX HERE: Cleaned up to exactly 3 arguments
            termios.tcsetattr(sys.stdin.fileno(), termios.TCSADRAIN, self.settings)

        """Main loop that waits for keys and publishes velocity messages."""
        twist = Twist()
        
        try:
            while True:
                key = self.get_key().lower()
                
                # Reset velocities every loop iteration
                twist.linear.x = 0.0
                twist.angular.z = 0.0

                if key == 'w':
                    twist.linear.x = self.linear_speed
                elif key == 's':
                    twist.linear.x = -self.linear_speed
                elif key == 'a':
                    twist.angular.z = self.angular_speed
                elif key == 'd':
                    twist.angular.z = -self.angular_speed
                elif key == 'q':
                    self.get_logger().info("Quitting WASD Teleop...")
                    break
                else:
                    # Ignore any other keys
                    continue

                # Send the movement command to TurtleSim
                self.publisher_.publish(twist)
                
        except Exception as e:
            self.get_logger().error(f"Error encountered: {e}")
        finally:
            # Always ensure the turtle stops moving when exiting
            twist.linear.x = 0.0
            twist.angular.z = 0.0
            self.publisher_.publish(twist)
            # Restore original terminal settings
            termios.tcsetattr(sys.stdin.fileno(), termios.TCSADRAIN, self.settings)


def main(args=None):
    rclpy.init(args=args)
    node = WasdTeleop()
    node.run()
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
