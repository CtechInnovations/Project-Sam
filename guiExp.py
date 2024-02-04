import tkinter as tk
from PIL import Image, ImageTk
import folium
from tkinter import ttk
import random
import webbrowser

class MapGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Fake Live GPS Map Viewer")
        self.root.geometry("1080x720")

        # Placeholder for GPS data (latitude, longitude)
        self.gps_data = (0.0, 0.0)

        # Placeholder for sensor data
        self.sensor_data = "No data"

        # Create canvas to display the map
        self.map_canvas = tk.Frame(self.root, width=800, height=600)
        self.map_canvas.pack()

        # Create a label for GPS data
        self.gps_label = tk.Label(self.root, text="GPS Data: ")
        self.gps_label.pack()

        # Create a label for sensor data
        self.sensor_label = tk.Label(self.root, text="Sensor Data: ")
        self.sensor_label.pack()

        # Create buttons
        self.button_frame = tk.Frame(self.root)
        self.button_frame.pack(pady=10)

        button1 = ttk.Button(self.button_frame, text="Button 1", command=self.button1_action)
        button1.grid(row=0, column=0, padx=10)
        button2 = ttk.Button(self.button_frame, text="Button 2", command=self.button2_action)
        button2.grid(row=0, column=1, padx=10)
        button3 = ttk.Button(self.button_frame, text="Button 3", command=self.button3_action)
        button3.grid(row=0, column=2, padx=10)
        button4 = ttk.Button(self.button_frame, text="Button 4", command=self.button4_action)
        button4.grid(row=0, column=3, padx=10)
        button5 = ttk.Button(self.button_frame, text="Button 5", command=self.button5_action)
        button5.grid(row=0, column=4, padx=10)

        # Create a button to update the map and sensor data
        self.update_data_button = ttk.Button(self.root, text="Update Data", command=self.update_data)
        self.update_data_button.pack()

        # Display the initial map and sensor data
        self.update_map()
        self.update_sensor_data()

    def update_data(self):
        # Simulate GPS data
        self.gps_data = self.generate_fake_gps_data()

        # Simulate sensor data
        self.sensor_data = self.generate_fake_sensor_data()

        # Update GPS data label
        self.gps_label.config(text=f"Latitude: {self.gps_data[0]}, Longitude: {self.gps_data[1]}")

        # Update sensor data label
        self.sensor_label.config(text=f"Sensor Data: {self.sensor_data}")

        # Schedule the next data update after 1000 milliseconds (1 second)
        self.root.after(1000, self.update_data)

    def generate_fake_gps_data(self):
        # Generate random GPS coordinates for testing
        latitude = round(random.uniform(-90, 90), 6)
        longitude = round(random.uniform(-180, 180), 6)
        return latitude, longitude

    def generate_fake_sensor_data(self):
        # Generate random sensor data for testing
        return round(random.uniform(0, 100), 2)

    def update_map(self):
        # Create a folium map centered at the current GPS coordinates
        folium_map = folium.Map(location=self.gps_data, zoom_start=15)
        folium.Marker(self.gps_data, popup='Current Location').add_to(folium_map)

        # Save the folium map as an HTML file
        folium_map.save('live_map.html')

        # Display the HTML file in the tkinter canvas using a web browser
        webbrowser.open('live_map.html')

    def button1_action(self):
        # Placeholder function for Button 1 action
        print("Button 1 clicked")

    def button2_action(self):
        # Placeholder function for Button 2 action
        print("Button 2 clicked")

    def button3_action(self):
        # Placeholder function for Button 3 action
        print("Button 3 clicked")

    def button4_action(self):
        # Placeholder function for Button 4 action
        print("Button 4 clicked")

    def button5_action(self):
        # Placeholder function for Button 5 action
        print("Button 5 clicked")

if __name__ == "__main__":
    root = tk.Tk()
    app = MapGUI(root)
    root.mainloop()

    #changes are still being made
    
