import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from turtlesim.srv import Spawn

class DualCircleTurtle(Node):

    def __init__(self):
        super().__init__('dual_circle_node')
        
        # 1. Create publishers for both turtles
        self.pub_turtle1 = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)
        self.pub_turtle2 = self.create_publisher(Twist, '/turtle2/cmd_vel', 10)
        
        # 2. Call the service to spawn the second turtle
        self.spawn_second_turtle()
        
        # 3. Create a timer to constantly publish movement commands (every 0.1 seconds)
        self.timer = self.create_timer(0.1, self.timer_callback)
        self.get_logger().info("Dual turtle circle node has started!")

    def spawn_second_turtle(self):
        """Calls the /spawn service to create turtle2."""
        client = self.create_client(Spawn, 'spawn')
        
        # Wait until the turtlesim node is up and service is available
        while not client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('Waiting for /spawn service to become available...')
            
        request = Spawn.Request()
        request.x = 2.0      # X coordinate in the window
        request.y = 5.5      # Y coordinate in the window
        request.theta = 0.0  # Orientation angle
        request.name = 'turtle2'
        
        # Send the request asynchronously
        future = client.call_async(request)
        self.get_logger().info('Sending request to spawn turtle2...')

    def timer_callback(self):
        """Publishes constant circular movements to both turtles."""
        # Twist message for Turtle 1 (Smaller, tighter circle)
        twist1 = Twist()
        twist1.linear.x = 2.0   # Forward speed
        twist1.angular.z = 1.0  # Rotation speed (positive = counter-clockwise)
        
        # Twist message for Turtle 2 (Larger or different circle)
        twist2 = Twist()
        twist2.linear.x = 3.0   # Faster forward speed
        twist2.angular.z = 1.0  # Same rotation speed creates a wider loop
        
        # Publish to both topics
        self.pub_turtle1.publish(twist1)
        self.pub_turtle2.publish(twist2)

def main(args=None):
    rclpy.init(args=args)
    node = DualCircleTurtle()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        node.get_logger().info("Stopping circle movements...")
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
