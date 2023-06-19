import socket

class lan_communication:
    def __init__(self) -> None:
        """
        Initialisiert eine Instanz der Klasse lan_communication.
        """
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_ip = "255.255.255.255"

    def setup_connection_as_server(self):
        """
        Setzt die Verbindung als Server auf.
        """
        self.server_socket.bind((self.server_ip, 12345))
        self.server_socket.listen(1)
        self.client_socket, self.address = self.server_socket.accept()

    def setup_connection_as_client(self):
        """
        Setzt die Verbindung als Client auf.
        """
        self.client_socket.connect((self.server_ip, 12345))

    def get_data(self):
        """
        Empfängt Daten von der Verbindung.
        
        Returns:
            Die empfangenen Daten als decodierten String.
        """
        data = self.client_socket.recv(1024)
        while data == b'':
            data = self.client_socket.recv(1024)
        return data.decode()

    def send_data_as_server(self, data):
        """
        Sendet Daten als Server über die Verbindung.
        
        Args:
            data: Die zu sendenden Daten als String.
        """
        self.server_socket.sendall(data.encode())

    def send_data_as_client(self, data):
        """
        Sendet Daten als Client über die Verbindung.
        
        Args:
            data: Die zu sendenden Daten als String.
        """
        self.client_socket.sendall(data.encode())

    def close_connection(self):
        """
        Schließt die Verbindung.
        """
        self.client_socket.close()
        self.server_socket.close()
