import time
import os
import psutil
import platform
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
console=Console()
gigabyte_value=lambda x,y:x/y
def show_processes():
 try:
  global pids
  global proc_names
  global proc_states
  pids=[]
  proc_names=[]
  proc_states=[]
  for process in psutil.process_iter(["pid","name","status"]):
      pids.append(str(process.pid))
      proc_names.append(process.name())
      if process.status()=="running":
       proc_states.append(process.status())
      else:
        continue
  else:
    full_proc_info=list(zip(proc_names,pids,proc_states))
    table='''  {pid}      {state}         {process_name}     '''
    console.print(" ID    STATE     COMMAND",style="black on green")
    for proc,id,state in full_proc_info:
        yield table.format(process_name=proc,pid=id,state=state[0].upper())
 except (psutil.AccessDenied,psutil.ZombieProcess,psutil.NoSuchProcess):
     pass

if __name__=="__main__":
 while True:
   display_processes=show_processes()
   for n in display_processes:
      print(n)
   os_name=platform.system()
   cpu_table=Table(style="green on black")
   cpu_table.add_column("[green]CPU[/]",style="green on black")
   cpu_table.add_column("[green]FREQ[/]",style="green on black")
   sys_table=Table()
   os.system("tree > folders_and_files.txt")
   os.system("pip list > package.txt")
   open_txt_file=open("folders_and_files.txt","r")
   open_txt_file_=open("package.txt","r")
   mem_panel=Panel(f"MEM STATS:\nTotal:{round(gigabyte_value(x=psutil.virtual_memory()[0],y=1e+9),2)}GB\nUSED:{psutil.virtual_memory()[2]}%\nFREE:{round(gigabyte_value(x=psutil.virtual_memory()[4],y=1e+9),2)} GB\nAVAIL:{round(gigabyte_value(x=psutil.virtual_memory()[1],y=1e+9),2)} GB",style="green on black",width=18)
   for core,n in enumerate(psutil.cpu_freq(percpu=True),start=0) :
    cpu_table.add_row(f'{core}:{psutil.cpu_percent(interval=1,percpu=True)[core]}%',f'{core}:{n.current}')
   if os_name in ["Linux","Darwin"]:
      os.system("clear")
      console.print(cpu_table,mem_panel,f"\nOS:{os_name}\nOS VERSION:{platform.version()}\n",f'{open_txt_file.readlines()[-1]}',f"number of python packages installed: {len(open_txt_file_.readlines()[2:])}","\naverage system load:"+" "+" ".join(list(map(lambda x:str(round(x,2)),psutil.getloadavg()))))
   else:
      os.system("cls")
      console.print(cpu_table,mem_panel,f"\nOS:{os_name}\nOS VERSION:{platform.version()}\n",f'{open_txt_file.readlines()[-1]}',f"number of python packages installed: {len(open_txt_file_.readlines()[2:])}")
