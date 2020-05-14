1.Topic:
A communication project between python and Demo3D( based C# ) .

2.Brief Introduction:
(1) win10.
(2) Demo3D 2015 as Client.
(3) Python3.8 as Server.
(4) We use ZeroMQ to transfer message  between python and Demo3D. ZeroMQ is an open-source universal messaging library. NetMQ is a 100% native C# port of ZeroMQ, a lightweight messaging library.
Here are some details about ZeroMQ and NetMQ.
https://zeromq.org/
https://netmq.readthedocs.io/en/latest/
(5) Message format : Json 


3. Configuration:
(1) In Demo3D, the NetMQ.dll located in ~/packages/NetMQ.3.3.0.11 will need copying into the Installation directory of Demo3D 2015.
(2) In python, we need to install ZeroMQ. Refer to https://zeromq.org/download/
① Download and Install ZeroMQ.zip	
② pip install pyzmq;
③ pip install json;

4. Runing
First, run the Python code.
Finally, run Demo3D_python_NetMQ(ZeroMQ)_Json.demo3d.