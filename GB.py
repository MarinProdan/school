#KiB=250*1024

#print("Velikost dat je",KiB,"b")

#data2=KiB*8
#konec=data2/1e8
#print(konec,"sekund")


def seconds_to_str(time_in_seconds: float) -> str:
    if time_in_seconds < 1e-6:
        return f"{round(time_in_seconds * 1e9,3)} nanoseconds"
    elif time_in_seconds < 1e-3:
        return f"{round(time_in_seconds * 1e6,3)} microseconds"
    elif time_in_seconds < 1:
        return f"{round(time_in_seconds * 1e3,3)} miliseconds"
    if time_in_seconds >= 3600:
        return f"{time_in_seconds / 3600:.1f} hours"
    elif time_in_seconds >= 60:
        return f"{time_in_seconds / 60:.1f} minutes"
    else:
        return f"{time_in_seconds/ 0.01} miliseconds"
    



def transfer_time(file_size, unit="MB",ethernet_speed=10) -> float:
    if unit == "KiB":
        return file_size*1024*8 / (ethernet_speed*1e6)
    if unit == "MB":
        return file_size*1024*1024*8 / (ethernet_speed*1e6)
    elif unit =="GiB":
        return file_size*1024*1024*1024*8 / (ethernet_speed*1e6)
time_seconds = transfer_time(1000, "MB", 100)
print(seconds_to_str(time_seconds))
print(f"{time_seconds:.2f} seconds")
