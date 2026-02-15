import time

def main():
    
    total_frames = 0
    frames = 0
    rsteps = 0 #refresh_steps
    psteps = 0 #previous_steps
    duration = 10 # <- RECOMMENDED VALUES, 1, 10, 15, 60, 300, etc
    total_steps = [] #difference
    total_steps_time = [] #time difference between steps
    start = time.perf_counter()
    initial_time = start

    while True:
        # Simulación de trabajo mínimo
        frames += 1
        rsteps += 1

        now = time.perf_counter()
        elapsed = now - start

        if elapsed >= 1.0:
            fps = frames / elapsed
            difference = rsteps - psteps
            print(f"FPS: {fps:.2f}")
            print(f"refresh_steps: {rsteps}, previous: {psteps}, difference:{difference}")
            if(frames>0):
                total_steps_time.append(f"{1/frames*10000:.5f}")        
            total_frames+=frames
            frames = 0
            total_steps.append(difference)
            psteps = rsteps
            start = now
        #Forzar salida pasado 'duration'
        if now - initial_time >= duration:
            break

    total_time = now - initial_time
    avg_fps_lcount = frames / total_time
    total_avg_fps = total_frames / total_time
    if(frames >= 0):
        avg_frametime_ms = (total_time / frames) * 1000
    else:
        print("Cantidad de frames igual a 0")


    # Informacion pertinente
    print(f"\n---------------------------\nSTATS:\n"
    +f"Duration: {total_time:.2f}s\n"
    +f"Last frame count: {avg_fps_lcount:.2f}\n"
    +f"Total frames in test: {total_frames}\n"
    +f"Total avg fps count: {total_avg_fps:.2f}\n"
    +f"avg_frametime_ms: {avg_frametime_ms:.5f}ms\n")

    print("Frame differences: ")
    print(total_steps)
    print("Frame time differences indicator (1/frames*10000): ")
    print(total_steps_time)

    file = open(f"./FPS.txt", 'w')
    file.writelines(
        f"Steps: {total_steps} \n"
        +f"Average_FPS_Last_Counted:{avg_fps_lcount:.2f}\n"
        +f"Duration: {duration}s\n"
        +f"Total_Steps: {total_steps}\n"
        +f"Total_time_difference_indicator: {total_steps_time}\n"
        )
    file.close()




if __name__ == "__main__":
    main()
