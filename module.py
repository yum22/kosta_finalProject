from gps3 import agps3
import requests
class gps():
	def __init__(self):
		self.gps_socket = agps3.GPSDSocket()
		self.data_stream = agps3.DataStream()
		self.gps_socket.connect()
		self.gps_socket.watch()
	def get_gps(self):
		for new_data in self.gps_socket:
			if new_data:
				self.data_stream.unpack(new_data)
				print('Altitude = ', self.data_stream.alt)
				print('Longitude = ', self.data_stream.lon)
				print('speed = ', self.data_stream.speed)
				self.send_gps(self.data_stream)
				#upload = {'alt':self.data_stream.alt, 'lon':self.data_stream.lon}
				#r=requests.post('http://192.168.0.126:9090/0615_springMVC/curlTest',data=upload)
	def send_gps(self,gpsdata):
		upload = {'alt':gpsdata.alt, 'lon':gpsdata.lon}
		r=requests.post('http://192.168.0.126:9090/0615_springMVC/curlTest',data=upload)
if __name__ == '__main__':
	gpsd = gps()
	gpsd.get_gps()