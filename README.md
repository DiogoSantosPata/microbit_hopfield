# microbit_hopfield
A simple <a href="https://en.wikipedia.org/wiki/Hopfield_network">hopfield</a> network implementation running on the BBC micro bit



### It goes as follow:

1. A bunch of random patterns are learnt by the network and one of them will be the target. <br>
2. When the user presses 'B', the target pattern will be randomly altered (up to 64%). <br>
3. Then, the network will try to restore the original pattern. <br>
4. Press 'A' to see the original pattern. <br>
5. Restart with microbit to set new patterns and learn again. <br>

<img src="microbit_hopfield.gif" width="380" height="300">

Visualization using the <a href="http://blog.withcode.uk/2016/05/microbit-python-simulator/">microbit-python-simulator</a>
