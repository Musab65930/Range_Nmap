# Range_Nmap
Range-Nmap is a simple terminal port scanner similar to Nmap, written in Python.
Usage
Single Port Scan
scan <ip> <port>


Example:

scan 10.10.10.5 80

Port Range Scan
scan <ip> <start>-<end>


Example:

scan 10.10.10.5 1-1000

Full Port Scan
scan <ip> all

Exit
exit

Installation

Clone the repository:

git clone https://github.com/Musab65930/Range_Nmap.git


Enter the folder:

cd Range_Nmap


Run the script:

python3 range_nova.py

Project Structure
Range_Nmap/
│
├── range_nova.py     # Main application
└── README.md         # Documentation
