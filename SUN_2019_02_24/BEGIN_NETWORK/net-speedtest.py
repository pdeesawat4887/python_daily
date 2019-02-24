import speedtest
import time


class NetworkSpeedtest:

    def __init__(self,  server=None):
        print("Speedtest on", time.strftime("%a, %d %b %Y %H:%M:%S"))
        if server == None:
            self.servers = []
        else:
            self.servers = [server]
        self.speedtest_work()
        self.get_output()
        self.extend()

    def speedtest_work(self):
        client = speedtest.Speedtest()
        client.get_servers(self.servers)
        client.get_best_server()
        client.download()
        client.upload(pre_allocate=False)
        client.results.share()
        self.result = client.results

    def convert_bps_to_mbps(self, bps):
        return round(bps / 1048576, 2)

    def convert_byte_to_megabyte(self, byte):
        return byte // 1048576

    def get_output(self):
        print("Download: {dl} Mbps\n"
              "Upload: {ul} Mbps\n"
              "Ping: {ping} ms\n"
              "Size of send packet: {size_send} Mb.\n"
              "Size of receive packet: {size_rec} Mb.\n"
              "Client: IP: {ip_client}, ISP: {isp_client}\n"
              "Server: Country: {country}, Sponsor: {sponsor}, Host: {host}\n".format(
            dl=self.convert_bps_to_mbps(self.result.download),
            ul=self.convert_bps_to_mbps(self.result.upload),
            ping=round(self.result.ping, 2),
            size_send=self.convert_byte_to_megabyte(self.result.bytes_sent),
            size_rec=self.convert_byte_to_megabyte(self.result.bytes_received),
            ip_client=self.result.client['ip'], isp_client=self.result.client['isp'],
            country=self.result.server['country'], sponsor=self.result.server['sponsor'],
            host=self.result.server['host']))

    def extend(self):
        # print(self.result.csv_header('|'))
        # print(self.result.csv('|'))
        print(self.result.json(pretty=True))


test = NetworkSpeedtest(server=8990)
