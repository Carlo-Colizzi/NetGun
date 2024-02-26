<center>
  <h1><strong>NetGun</strong></h1>
</center>

<p align="center">
    <img src="https://github.com/Carlo-Colizzi/NetGun/blob/main/source_code/persistence/storage/assets/netgun_logo.png"alt="NETGUN">
</p>

<center>
<i>Repo metadata</i>

  <a href="https://github.com/Carlo-Colizzi/NetGun/releases/"><img src="https://img.shields.io/github/release/MyCr4ck/NetGun_Classe03?include_prereleases=&sort=semver&color=blue" alt="GitHub release"></a>
  <a href="https://github.com/Carlo-Colizzi/NetGun/issues"><img src="https://img.shields.io/github/issues/MyCr4ck/NetGun_Classe03" alt="issues - NetGun_Classe03"></a>
  <a href="https://github.com/Carlo-Colizzi/NetGun/blob/main/LICENSE"><img src="https://img.shields.io/badge/License-GNU_GPLv3-purple" alt="License"></a>

</center>

<i>Documentation</i>
<div align="left">
  <a href="https://github.com/MyCr4ck/NetGun_Classe03/tree/main/Documentation" title="Go to project documentation"><img src="https://img.shields.io/badge/view-Documentation-blue?style=for-the-badge" alt="view - Documentation"></a>
</div>

## Introduction
NetGun is a Vulnerability Scanner written in Python. It allows to scan Network infrastructures, enumerate the services running on them, unearth CVEs and Misconfigurations.
It aims to facilitate a complex practice such as Penetration Testing, so that PTs can focus on more delicate aspects, automating and speeding up the tasks behind this type of Testing.

## NetGun allows you to
<ul>
  <li> Detect open and closed ports on any accessible target host </li>
  <li> Detect the Operating System</li>
  <li> Detect the services running  on each port</li>
  <li> Detect firewalls</li>
  <li> Detect tipical misconfigurations</li>
  <li> Detect CVEs on services</li>
</ul>


## Installation
```bash
git clone https://github.com/Carlo-Colizzi/NetGun
cd NetGun
pip install -r requirements.txt
```

## How to Use
<p>> Here you can set the details of the scan</p>
<div align="center">
  <img src="https://github.com/Carlo-Colizzi/NetGun/blob/main/source_code/persistence/storage/assets/scan_details.png">
</div>

<p>> You can set IPv4 and Port range</p>
<div align="center">
  <img src="https://github.com/Carlo-Colizzi/NetGun/blob/main/source_code/persistence/storage/assets/set_ip_and_ports.png">
</div>

<p>> Choose the protocol used by the researched services, TCP or UDP</p>
<div align="center">
  <img src="https://github.com/Carlo-Colizzi/NetGun/blob/main/source_code/persistence/storage/assets/protocol.png">
</div>
  <p>> Choose the Advanced Options:</p>
  <ul>
    <li><strong>OS detection</strong>: let to discover the OS used by the Target</li>
    <li><strong>Disable PING</strong>: during the scan the ping functionality will not be used</li>
    <li><strong>SYN scan</strong>: SYN scan is the default and most popular scan option for good reason. It can be performed quickly, scanning thousands of ports per second on a fast network not hampered by intrusive firewalls. SYN scan is relatively unobtrusive and stealthy, since it never completes TCP connections.</li>
    <li><strong>ACK scan</strong>:  Its probe packet has only the ACK flag set. When scanning unfiltered systems, open and closed ports will both return a RST packet. NetGun then labels them as unfiltered, meaning that they are reachable by the ACK packet, but whether they are open or closed is undetermined. Ports that don't respond, or send certain ICMP error messages back, are labeled filtered.</li>
    <br>
    <p><strong>Important: </strong>   you can't use SYN scan and ACK scan together</p>
  </ul>

<div align="center">
  <img src="https://cdn.discordapp.com/attachments/1051051902529437787/1077702303034908712/Immagine_2023-02-16_140002.png">
</div>
  <p>> Choose the scan mode:</p>
  <ul>
    <li><strong>SHALLOW</strong>: a shallow and stealth scan, do not look for services version</li>
    <li><strong>DEEP</strong>: a deep scan, look also for services version</li>
  </ul>
<div align="center">
  <img src="https://github.com/Carlo-Colizzi/NetGun/blob/main/source_code/persistence/storage/assets/set_deep_or_shallow.png">
</div>
<p>> Choose the scan aggressivity, from 0 (slow and stealth) to 4 (fast)</p>
<div align="center">
  <img src="https://github.com/Carlo-Colizzi/NetGun/blob/main/source_code/persistence/storage/assets/scan_aggressivity.png">
</div>
<p>> When the scan terminate, you will see the results in such a table:</p>
<div align="center">
  <img src="https://github.com/Carlo-Colizzi/NetGun/blob/main/source_code/persistence/storage/assets/scan_result.png">
</div>

### CVE analysis
<p>> You can check all the CVEs of a specific service just selecting it and clicking "Open CVE". The Vulnerabilities are obtained through the National Vulnerability Database of U.S. government</p>
<div align="center">
  <img src="https://github.com/Carlo-Colizzi/NetGun/blob/main/source_code/persistence/storage/assets/search_cve.png">
</div>

### Speedtest by OOkla
<p>> You can also make a Speedtest:</p>
<div align="center">
  <img src="https://github.com/Carlo-Colizzi/NetGun/blob/main/source_code/persistence/storage/assets/speedtest.png">
</div>

## Other Images
<div align="center">
  <img src="https://github.com/Carlo-Colizzi/NetGun/blob/main/source_code/persistence/storage/assets/scan_loading.png">
  <img src="https://github.com/Carlo-Colizzi/NetGun/blob/main/source_code/persistence/storage/assets/scan_and_cve_view.png">
  <img src="https://github.com/Carlo-Colizzi/NetGun/blob/main/source_code/persistence/storage/assets/welcome.png">
  <img src="https://github.com/Carlo-Colizzi/NetGun/blob/main/source_code/persistence/storage/assets/scan_view.png">
</div>
