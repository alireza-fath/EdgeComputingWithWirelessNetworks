# Purpose
This repository is created to make available the data and source code related to the experiments conducted in "GPR sensing and visual mapping through 4G-LTE, 5G, Wi-Fi HaLow, and Wi-Fi hotspots with edge computing and AR Representation".

## Structure
The experiments described were conducted using a client-server model using various connection methods, namely HaLow, 2.4 and 5GHz Wi-Fi, and 4G and 5G cellular. For all tests, the scripts `clienttest3` and `servertest3` were used to generate the data. Data for the local connection methods described in section 3.2 are found in the `LocalNetworkLatencyTestData` directory. Data for the cellular connection methods described in section 3.3 are found in the `CellularLatencyTestByPacketSize` directory.

## Citations

Fath, Alireza. 2024. "Integration and Performance Assessment of Cyber-Physical Systems for Structural Health Monitoring and Maintenance." Order No. 31487424, The University of Vermont and State Agricultural College. https://login.ezproxy.uvm.edu/login?url=https://www.proquest.com/dissertations-theses/integration-performance-assessment-cyber-physical/docview/3086817567/se-2.

Tanch, S.; Fath, A.; Hanna, N.; Xia, T.; Huston, D. GPR Sensing and Visual Mapping Through 4G-LTE, 5G, Wi-Fi HaLow, and Wi-Fi Hotspots with Edge Computing and AR Representation. Appl. Sci. 2025, 15, 6552. https://doi.org/10.3390/app15126552

## License

MIT License

This project also uses the following libraries, which are licensed under their respective licenses:

- `socket`: PSF License
- `time`: PSF License
- `matplotlib`: BSD-style License

You can find the full text of these licenses in the `LICENSE` file.

### MIT License

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
