import psutil
import time
import subprocess
import keyboard
from rich.console import Console
from rich.table import Table
console=Console()
total_memory=psutil.virtual_memory()
used_mem=total_memory[3]*1e+9

if __name__=="__main__":
 while True:
   mapped=map(str,psutil.pids())
   table=Table(style="green on black")
   table.add_column("[green]CPU[/]",style="green on black")
   table.add_column("[green]FREQUENCY[/]",style="green on black")
   table.add_column("[green]MEMORY[/]",style="green on black")
   table.add_column("[green]PIDS[/]",style="green on black")
   table.add_row(f'0:{psutil.cpu_percent(interval=0.1,percpu=True)[0]}%',f'{psutil.cpu_freq(percpu=True)[0][0]} MHz',f'USED:{psutil.virtual_memory()[2]}%')
   table.add_row(f'1:{psutil.cpu_percent(interval=0.1,percpu=True)[1]}%',f'{psutil.cpu_freq(percpu=True)[1][0]} MHz',f'AVAIL:{round(psutil.virtual_memory()[1]/1e+9,2)} GB',f'{"\n".join([x for x in mapped])}')
   time.sleep(1)
   subprocess.call("clear")
   console.print(table,end="\r")
   if keyboard.is_pressed("q")==True:
      quit("Program exitted")
   else:
     pass
