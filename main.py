import time
import subprocess
import os
import psutil
from rich.console import Console
from rich.table import Table
console=Console()
processes=[]
bar_char="█"
gigabyte_value=lambda x,y:x/y
def show_disk_usage():
  directories=[]
  for dir in os.listdir():
      if os.path.isdir(dir)==True:
         directories.append(dir)
      else:
         continue
  else:
       for folder in directories:
          if psutil.disk_usage(path=folder)[-1]<50:
             console.print(f"\b{folder}| [green][{bar_char*4}][/]-{psutil.disk_usage(path=folder)[-1]}%\n")
          elif  psutil.disk_usage(path=folder)[-1]>=51 and psutil.disk_usage(path=folder)[-1]<=75:
             console.print(f"\b{folder}| [orange1][{bar_char*8}][/]-{psutil.disk_usage(path=folder)[-1]}%\n")
          elif  psutil.disk_usage(path=folder)[-1]>=51 and psutil.disk_usage(path=folder)[-1]<=75:
             console.print(f"\b{folder}| [red][{bar_char*16}][/]-{psutil.disk_usage(path=folder)[-1]}%\n")
          elif psutil.disk_usage(path=folder)[-1]>=80:
             console.print(f"\n\b{folder}|[[red]{bar_char*32}[/]]-{psutil.disk_usage(path=folder)[-1]}%\n")


for process in psutil.process_iter():
    processes.append(str(process.pid)+"-"+process.name())
if __name__=="__main__":
 while True:
   show_disk_usage()
   table=Table(style="green on black")
   table.add_column("[green]CPU[/]",style="green on black")
   table.add_column("[green]FREQUENCY[/]",style="green on black")
   table.add_column("[green]MEMORY[/]",style="green on black")
   table.add_column("[green]PIDS[/]",style="green on black")
   table.add_row(f'0:{psutil.cpu_percent(interval=0.1,percpu=True)[0]}%',f'{psutil.cpu_freq(percpu=True)[0][0]} MHz',f'USED:{psutil.virtual_memory()[2]}%')
   table.add_row(f'1:{psutil.cpu_percent(interval=0.1,percpu=True)[1]}%',f'{psutil.cpu_freq(percpu=True)[1][0]} MHz',f'AVAIL:{round(gigabyte_value(x=psutil.virtual_memory()[1],y=1e+9),2)} GB\nTOTAL:{round(gigabyte_value(x=psutil.virtual_memory()[0],y=1e+9),2)} GB\nFREE:{round(gigabyte_value(x=psutil.virtual_memory()[4],y=1e+9),2)} GB'," ".join(processes))

   time.sleep(1)
   subprocess.call("clear")
   console.print(table,end="\r")
