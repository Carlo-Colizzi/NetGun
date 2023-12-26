<center>
  <h1><strong>NetGun</strong></h1>
</center>

<p align="center">
    <img src="https://cdn.discordapp.com/attachments/1051051902529437787/1077697212634636308/NetgunLogo13_Telefono.png"alt="NETGUN">
</p>

<center>
<i>Repo metadata</i>

  <a href="https://github.com/MyCr4ck/NetGun_Classe03/releases/"><img src="https://img.shields.io/github/release/MyCr4ck/NetGun_Classe03?include_prereleases=&sort=semver&color=blue" alt="GitHub release"></a>
  <a href="https://github.com/MyCr4ck/NetGun_Classe03/issues"><img src="https://img.shields.io/github/issues/MyCr4ck/NetGun_Classe03" alt="issues - NetGun_Classe03"></a>
  <a href="https://github.com/MyCr4ck/NetGun_Classe03/blob/main/LICENSE"><img src="https://img.shields.io/badge/License-GNU_GPLv3-purple" alt="License"></a>

</center>

<div align="center">
</div>
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
  <li> Detect the Operative System</li>
  <li> Detect the services running  on each port</li>
  <li> Detect firewalls</li>
  <li> Detect tipical misconfitgurations</li>
  <li> Detect CVEs on services</li>
</ul>


## Installation
'''bash
prova
'''

## How to Use
### Main feature
<div>
  <div align="center">
  <i>Localhost: 127.0.0.1</i>
  <img src="https://cdn.discordapp.com/attachments/1051051902529437787/1077700432786358272/Immagine_2023-02-16_135725.png">
</div>
Il programma funziona tramite un'<strong>API NMAP</strong>, avrà quindi bisogno di vari dati in input.
I primi tra tutti sono L'<strong>IP</strong> e le <strong>PORTE</strong>:
<div>
  <div align="center">
  <img src="https://cdn.discordapp.com/attachments/1051051902529437787/1077701097428369478/Immagine_2023-02-16_135935.png">
</div>
Poi si passa al <strong>Protocollo</strong>:
<div>
  <div align="center">
  <img src="https://cdn.discordapp.com/attachments/1051051902529437787/1077701557904228352/Immagine_2023-02-16_135946.png">
</div>
Nella sezione <strong>Advanced</strong> bisogna aggiungere i filtri ulteriori di ricerca, nel nostro caso ci sono 3 possibilità che possono andare in simultanea,<strong>ACK scan e SYN scan</strong> non possono essere usate insieme.
Quindi selezionare i filtri aggiuntivi e premere OK:
<div>
  <div align="center">
  <img src="https://cdn.discordapp.com/attachments/1051051902529437787/1077702303034908712/Immagine_2023-02-16_140002.png">
</div>
Scegliere l'intesità e il numero di dati da prendere in considerazione attraverso <strong>SHALLOW e DEEP</strong>:
<div>
  <div align="center">
  <img src="https://cdn.discordapp.com/attachments/1051051902529437787/1077703822513811618/Immagine_2023-02-16_140012.png">
</div>
Ed infine il tempo dello scan che va dal più lento, 0, a 4 il più veloce, usata in particolare in funzione stealth o per non caricare e appesantire la macchina target, definita <strong>Aggressività</strong>:
<div>
  <div align="center">
  <img src="https://cdn.discordapp.com/attachments/1051051902529437787/1077704441064591400/Immagine_2023-02-16_140023.png">
</div>
Una volta fatto partire lo scan si avrà questa tabella:
<div>
  <div align="center">
  <img src="https://cdn.discordapp.com/attachments/1051051902529437787/1077704860113309777/ImmagineNetgun_6.png">
</div>

### CVE analysis
Il nostro programma presenta la funzione di <strong>searchCVE</strong>, trova quindi tutte le malconfigurazioni trovate in tempo reale, basta quindi cliccare un oggetto sulla tabella e schiacciare openCVE:
<div>
  <div align="center">
  <img src="https://cdn.discordapp.com/attachments/1051051902529437787/1077706089442844762/ImmagineNetgun_7.png">
</div>

### Speedtest by OOkla
Il nostro programma presenta nella sezione messaggio di benvenuto un comodo Speedtest powered by OOkla, se non è la prima volta basta cliccare sull'icona del profilo in basso a destra e poi su Speedtest:
<div>
  <div align="center">
  <img src="https://cdn.discordapp.com/attachments/1051051902529437787/1077707035849785455/image.png">
</div>

## Galleria
<i>I dati variano da scan a scan, il link e riferimenti sono puramente casuali</i>
<div>
  <div align="center">
  <img src="https://cdn.discordapp.com/attachments/1051051902529437787/1077630204933058671/ImmagineNetgun_1.png">
  <img src="https://cdn.discordapp.com/attachments/1051051902529437787/1077630204555579555/ImmagineNetgun_2.png">
  <img src="https://cdn.discordapp.com/attachments/1051051902529437787/1077630204199055370/ImmagineNetgun_4.png">
  <img src="https://cdn.discordapp.com/attachments/1051051902529437787/1077630203997720646/ImmagineNetgun_5.png">
</div>
