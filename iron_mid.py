
from dst_parser_no_print import parse_dst_file_no_tiling
from event_display_modified import waveforms, footprint
import numpy as np
import matplotlib.pyplot as plt
from dstparser.dst_adapter import get_sd_position
import math

separation_time = 4

file_error = 0
other_error = 0
total = 0

low_uncorr_prior = 0
low_uncorr_later = 0
up_uncorr_prior = 0
up_uncorr_lower = 0

up_arrival_prior = []
up_arrival_later = []
low_arrival_prior = []
low_arrival_later = []


up_duration_prior = []
up_duration_later = []
low_duration_prior = []
low_duration_later = []

lateral_distance_up_prior = []
lateral_distance_up_later = []
lateral_distance_low_prior = []
lateral_distance_low_later = []

for i in range(9999):
    nnnn = f"{i:04}"
    for j in range(9, 17):
        XX = f"{j:02}"
        YYMMDD = str(nnnn) + str(XX)
        try:
            dst_file = "/ceph/work/SATORI/projects/TA-ASIoP/tasdmc_dstbank/qgsii04iron/080417_160603/Em1_bsdinfo/DAT%s_gea.rufldf.dst.gz"%(YYMMDD)
            data = parse_dst_file_no_tiling(dst_file)
            index_list = np.where((data["std_recon"]["nstclust"] > 5))[0]
            for event in index_list:
                
                try:
                    isgood_option = "nstclust"

                    arrival_time = []
                    uncorr_sdid_up_prior = []
                    uncorr_sdid_up_later = []
                    uncorr_sdid_low_prior = []
                    uncorr_sdid_low_later = []
                    core = None
                    core_index = None
                    core_x_position = None
                    core_y_position = None

                    fig, ax, sd_wf, sd_id = waveforms(data,
                                                        index = event,
                                                        #colors = colors,
                                                        #sdid_colors = sdid_colors,
                                                        with_start_time = True,
                                                        isgood_option = isgood_option)
                    
                    core_x_position = ((data["std_recon"]["shower_core"][event][0]) / 1000)
                    core_y_position = ((data["std_recon"]["shower_core"][event][1]) / 1000)
                
                    axis_z = abs(data["std_recon"]["shower_axis"][event][0])
        
                
                    for i, sd_index in enumerate(sd_id):
                        signal_interval = len(sd_wf[i]) 
                        switch_up = False
                        switch_low = False
                        curr_up_duration = 0
                        curr_low_duration = 0

                        curr_state = 0
                        prev_state = 0
                        check = None
                        for wf_index in range(signal_interval):
                    
                        
                            #edge = 0 no waveform, edge = 1 starting wave, edge = 2 during wave, edge = 3 ending edge
                            for bin in range(128):
                                if (sd_wf[i][wf_index][0][bin] >= 5) and (sd_wf[i][wf_index][1][bin] >= 5 * sd_wf[i][wf_index][0][bin]) and (sd_wf[i][wf_index][0][bin] <= 40):
                                    curr_up_duration += 1
                                    if switch_up:
                                        curr_state = 2
                                        check = "during_up"
                                        end_bin_up = bin
                                        
                                    else:
                                        curr_state = 1
                                        check = "start_up"
                                        switch_up = True
                                        switch_low = False
                                        start_bin_up = bin
                                 
                                    


                                elif (sd_wf[i][wf_index][1][bin] >= 5) and (sd_wf[i][wf_index][0][bin] >= 5 * sd_wf[i][wf_index][1][bin]) and (sd_wf[i][wf_index][1][bin] <= 40):
                                    curr_low_duration += 1
                                    if switch_low:
                                        curr_state = 2
                                        check = "during_low"
                                        end_bin_low = bin
                                        
                                    else:
                                        curr_state = 1
                                        check = "start_low"
                                        switch_low = True
                                        switch_up = False
                                        start_bin_low = bin
                                        
                                        
                                    

                                else:
                                    switch_up = False
                                    switch_low = False
                                    curr_state = 0
                                    if prev_state == 1 or prev_state == 2:
                                        prev_state == 3
                                        if check == "during_up":
                                            check = "end_up"
                                        elif check == "during_low":
                                            check = "end_low"
                                    else:
                                        check = None

                                if check == "start_up":
                                    for check_range in range(1, 6):
                                        try:
                                            if (sd_wf[i][wf_index][1][bin - check_range] >= 3 * (sd_wf[i][wf_index][0][bin - check_range])):
                                                curr_up_duration += 1
                                                start_bin_up = bin - check_range

                                        except:
                                            break
                                    if (20 * ((128 * wf_index) + ((start_bin_up))) / 1000) < separation_time:
                                        uncorr_sdid_up_prior.append(sd_index)
                                    else:
                                        uncorr_sdid_up_later.append(sd_index)
                                  
                                        


                                    

                                
                                elif check == "start_low":
                                    for check_range in range(1, 6):
                                        try:
                                            if (sd_wf[i][wf_index][0][bin - check_range] >= 3 * (sd_wf[i][wf_index][1][bin - check_range])):
                                                
                                                curr_low_duration += 1
                                                start_bin_low = bin - check_range

                                        except:
                                            break
                                    if (20 * ((128 * wf_index) + ((start_bin_low))) / 1000) < separation_time:
                                        uncorr_sdid_low_prior.append(sd_index)
                                    else:
                                        uncorr_sdid_low_later.append(sd_index)

                                   

                                elif check == "end_up":
                                    for check_range in range(1, 6):
                                        try:
                                            if (sd_wf[i][wf_index][1][bin + check_range] >= 3 * (sd_wf[i][wf_index][0][bin + check_range])):
                                                curr_up_duration += 1
                                                end_bin_up = bin + check_range
                                                

                                        except:
                                            break
                                    if (20 * ((128 * wf_index) + ((start_bin_up))) / 1000) < separation_time:
                                        up_arrival_prior.append(20 * ((128 * wf_index) + ((start_bin_up))) / 1000)
                                        up_duration_prior.append(curr_up_duration * 20)
                                    else:
                                        up_arrival_later.append(20 * ((128 * wf_index) + ((start_bin_up))) / 1000)
                                        up_duration_later.append(curr_up_duration * 20)
                                        
                                   
                                    curr_up_duration = 0
                                
                                elif check == "end_low":
                                    for check_range in range(1, 6):
                                        try:
                                            if (sd_wf[i][wf_index][0][bin + check_range] >= 3 * (sd_wf[i][wf_index][1][bin + check_range])):
                                                curr_low_duration += 1

                                        except:
                                            break

                                    if (20 * ((128 * wf_index) + ((start_bin_low))) / 1000) < separation_time:
                                        low_arrival_prior.append(20 * ((128 * wf_index) + ((start_bin_low))) / 1000)
                                        low_duration_prior.append(curr_low_duration * 20)

                                    else:
                                        low_arrival_later.append(20 * ((128 * wf_index) + ((start_bin_low))) / 1000)
                                        low_duration_later.append(curr_low_duration * 20)

                                   
                                    curr_low_duration = 0
                                   





                                else:
                                    pass

                                prev_state = curr_state
                        
                    
                    for sdid in uncorr_sdid_up_prior:
                           
                        signal_positions = get_sd_position(sdid)
                        x_position = (signal_positions[0][0] / 1000)
                        y_position = (signal_positions[0][1] / 1000)           
                        distance = (((((x_position - core_x_position)**2) + ((y_position - core_y_position)**2)) ** (1/2)) * axis_z) * 1000
                        lateral_distance_up_prior.append(distance)


                    for sdid in uncorr_sdid_up_later:
                           
                        signal_positions = get_sd_position(sdid)
                        x_position = (signal_positions[0][0] / 1000)
                        y_position = (signal_positions[0][1] / 1000)
                        distance = (((((x_position - core_x_position)**2) + ((y_position - core_y_position)**2)) ** (1/2)) * axis_z) * 1000
                        lateral_distance_up_later.append(distance)

                    for sdid in uncorr_sdid_low_prior:
                        signal_positions = get_sd_position(sdid)
                        x_position = (signal_positions[0][0] / 1000)
                        y_position = (signal_positions[0][1] / 1000)
                        distance = (((((x_position - core_x_position)**2) + ((y_position - core_y_position)**2)) ** (1/2)) * axis_z) * 1000
                        lateral_distance_low_prior.append(distance)

                    for sdid in uncorr_sdid_low_later:
                        signal_positions = get_sd_position(sdid)
                        x_position = (signal_positions[0][0] / 1000)
                        y_position = (signal_positions[0][1] / 1000)
                        distance = (((((x_position - core_x_position)**2) + ((y_position - core_y_position)**2)) ** (1/2)) * axis_z) * 1000
                        lateral_distance_low_later.append(distance)
                    
                    
                except FileNotFoundError:
               
                    file_error += 1
                except:
                    other_error += 1
                else:
                    total += 1



        except:
            other_error += 1
            

print("file error" + str(file_error/total * 100) + "%") 
print("other error" + str(other_error/total * 100) + "%")
print()
print("Number of instances where signal only appears on upper layer prior to separation time " + str(len(up_arrival_prior)))
print("Number of instances where signal only appears on upper layer later than separation time " + str(len(up_arrival_later)))
print("Number of instances where signal only appears on lower layer prior to separation time " + str(len(low_arrival_prior)))
print("Number of instances where signal only appears on lower layer later than separation time " + str(len(low_arrival_later)))
print()
print("Averge arrival time of upper layer uncorrelation(μs) prior to separation time " + str(sum(up_arrival_prior)/len(up_arrival_prior)))
print("Averge arrival time of upper layer uncorrelation(μs) later than separation time " + str(sum(up_arrival_later)/len(up_arrival_later)))
print("Averge arrival time of lower layer uncorrelation(μs) prior to separation time " + str(sum(low_arrival_prior)/len(low_arrival_prior)))
print("Averge arrival time of lower layer uncorrelation(μs) later than separation time " + str(sum(low_arrival_later)/len(low_arrival_later)))
print()
print("Averge duration of up uncorrelation(ns) prior to separation time " + str(sum(up_duration_prior)/len(up_duration_prior)))
print("Averge duration of up uncorrelation(ns) later than separation time " + str(sum(up_duration_later)/len(up_duration_later)))
print("Averge duration of low uncorrelation(ns) prior to separation time " + str(sum(low_duration_prior)/len(low_duration_prior)))
print("Averge duration of low uncorrelation(ns) later than separation time " + str(sum(low_duration_later)/len(low_duration_later)))
print()

# up_arrival_time_unfilterd = up_arrival_prior + up_arrival_later
# up_arrival_time = [x for x in up_arrival_time_unfilterd if x <= 12]
# low_arrival_time_unfilterd = low_arrival_prior + low_arrival_later
# low_arrival_time = [x for x in low_arrival_time_unfilterd if x <= 12]

# arrival_min = min(np.min(up_arrival_time), np.min(low_arrival_time))
# arrival_max = max(np.max(up_arrival_time), np.max(low_arrival_time))
# arrival_bins = np.linspace(arrival_min, arrival_max,  16)

# plt.figure(figsize=(10, 8))
# plt.subplot(1, 2, 1)
# plt.hist(up_arrival_time, bins = arrival_bins,color='blue', edgecolor='black', alpha=0.7)
# plt.xlim(0, 12)
# plt.title("Up Arrival Time Histogram")
# plt.xlabel('Time(μs)')
# plt.ylabel('Frequency')
# plt.subplot(1, 2, 2)
# plt.hist(low_arrival_time, bins = arrival_bins,color='red', edgecolor='black', alpha=0.7)
# plt.xlim(0, 12)
# plt.title("Low Arrival Time Histogram")
# plt.xlabel('Time(μs)')
# plt.ylabel('Frequency')
# plt.savefig("Arrival_IRON_MID.png")
# plt.close()

# plt.figure(figsize=(10, 8))
# plt.subplot(1, 2, 1)
# plt.hist(up_arrival_time, bins = arrival_bins,color='blue', edgecolor='black', alpha=0.7)
# plt.xlim(0, 12)
# plt.title("Up Arrival Time Histogram (Log Scale)")
# plt.xlabel('Time(μs)')
# plt.ylabel('Frequency')
# plt.yscale("log")
# plt.subplot(1, 2, 2)
# plt.hist(low_arrival_time, bins = arrival_bins,color='red', edgecolor='black', alpha=0.7)
# plt.xlim(0, 12)
# plt.title("Low Arrival Time Histogram")
# plt.xlabel('Time(μs)')
# plt.ylabel('Frequency')
# plt.yscale("log")
# plt.savefig("Arrival_IRON_MID_LOG.png")
# plt.close()





up_duration_prior = [x for x in up_duration_prior if x <= 700]
up_duration_later = [x for x in up_duration_later if x <= 700]
low_duration_prior = [x for x in low_duration_prior if x <= 700]
low_duration_later = [x for x in low_duration_later if x <= 700]

duration_min = min(np.min(up_duration_prior), np.min(up_duration_later), np.min(low_duration_prior), np.min(low_duration_later))
duration_max = max(np.max(up_duration_prior), np.max(up_duration_later), np.max(low_duration_prior), np.max(low_duration_later))
duration_bins = np.linspace(duration_min, duration_max,  16)



plt.figure(figsize=(15, 15))
plt.subplot(2, 2, 1)
plt.hist(up_duration_prior, bins = duration_bins,color='blue', edgecolor='black', alpha=0.7)
plt.title("Up Duration Prior Histogram")
plt.xlim(0, 700)
plt.xlabel('Time(ns)')
plt.ylabel('Frequency')

plt.subplot(2, 2, 2)
plt.hist(up_duration_later, bins = duration_bins ,color='blue', edgecolor='black', alpha=0.7)
plt.title("Up Duration Later Histogram")
plt.xlim(0, 700)
plt.xlabel('Time(ns)')
plt.ylabel('Frequency')


plt.subplot(2, 2, 3)
plt.hist(low_duration_prior, bins = duration_bins ,color='red', edgecolor='black', alpha=0.7)
plt.title("Low Duration Prior Histogram")
plt.xlim(0, 700)
plt.xlabel('Time(ns)')
plt.ylabel('Frequency')


plt.subplot(2, 2, 4)
plt.hist(low_duration_later, bins = duration_bins ,color='red', edgecolor='black', alpha=0.7)
plt.title("Low Duration Later Histogram")
plt.xlim(0, 700)
plt.xlabel('Time(ns)')
plt.ylabel('Frequency')

plt.savefig("Duration_IRON_MID.png")
plt.close()


################################################################################
plt.figure(figsize=(15, 15))
plt.subplot(2, 2, 1)
plt.hist(up_duration_prior, bins = duration_bins,color='blue', edgecolor='black', alpha=0.7)
plt.title("Up Duration Prior Histogram")
plt.xlim(0, 700)
plt.xlabel('Time(ns)')
plt.ylabel('Frequency')
plt.yscale("log")

plt.subplot(2, 2, 2)
plt.hist(up_duration_later, bins = duration_bins ,color='blue', edgecolor='black', alpha=0.7)
plt.title("Up Duration Later Histogram")
plt.xlim(0, 700)
plt.xlabel('Time(ns)')
plt.ylabel('Frequency')
plt.yscale("log")


plt.subplot(2, 2, 3)
plt.hist(low_duration_prior, bins = duration_bins ,color='red', edgecolor='black', alpha=0.7)
plt.title("Low Duration Prior Histogram")
plt.xlim(0, 700)
plt.xlabel('Time(ns)')
plt.ylabel('Frequency')
plt.yscale("log")


plt.subplot(2, 2, 4)
plt.hist(low_duration_later, bins = duration_bins ,color='red', edgecolor='black', alpha=0.7)
plt.title("Low Duration Later Histogram")
plt.xlim(0, 700)
plt.xlabel('Time(ns)')
plt.ylabel('Frequency')
plt.yscale("log")
plt.savefig("Duration_IRON_MID_LOG.png")
plt.close()




up_arrival_time_unfilterd = up_arrival_prior + up_arrival_later
up_arrival_time = [x for x in up_arrival_time_unfilterd if x <= 12]
low_arrival_time_unfilterd = low_arrival_prior + low_arrival_later
low_arrival_time = [x for x in low_arrival_time_unfilterd if x <= 12]
arrival_log_bins = np.logspace(np.log10(1), np.log10(12), 12)
up_arrival_out = [[bin_value, np.sum((up_arrival_time > (bin_value - 1)) & (up_arrival_time <= bin_value))] for bin_value in arrival_log_bins]
low_arrival_out = [[bin_value, np.sum((low_arrival_time > (bin_value - 1)) & (low_arrival_time <= bin_value))] for bin_value in arrival_log_bins]



LD_bin = 16


# Up Prior
lateral_distance_copy_up_prior = [x for x in lateral_distance_up_prior if x <= 2500]
radius_log_up_prior = np.logspace(np.log10(1), np.log10(2500), LD_bin)
logwidths_up_prior = np.diff(radius_log_up_prior)
centers_up_prior = np.sqrt(radius_log_up_prior[1:] * radius_log_up_prior[:-1])
counts_up_prior = np.histogram(lateral_distance_copy_up_prior, bins=radius_log_up_prior)[0]
areas_log_up_prior = 2*np.pi*(radius_log_up_prior[1:]**2 - radius_log_up_prior[:-1]**2) 
LD_up_prior_out = [[centers_up_prior[i], (counts_up_prior[i] * areas_log_up_prior[i] / 3 * 507/700000000)] for i in range(LD_bin - 1)]

# Up Later
lateral_distance_copy_up_later = [x for x in lateral_distance_up_later if x <= 2500]
radius_log_up_later = np.logspace(np.log10(1), np.log10(2500), LD_bin)
logwidths_up_later = np.diff(radius_log_up_later)
centers_up_later = np.sqrt(radius_log_up_later[1:] * radius_log_up_later[:-1])
counts_up_later = np.histogram(lateral_distance_copy_up_later, bins=radius_log_up_later)[0]
areas_log_up_later = 2*np.pi*(radius_log_up_later[1:]**2 - radius_log_up_later[:-1]**2) 
LD_up_later_out = [[centers_up_later[i], (counts_up_later[i] * areas_log_up_later[i] / 3 * 507/700000000)] for i in range(LD_bin - 1)]

# Low Prior
lateral_distance_copy_low_prior = [x for x in lateral_distance_low_prior if x <= 2500]
radius_log_low_prior = np.logspace(np.log10(1), np.log10(2500), LD_bin)
logwidths_low_prior = np.diff(radius_log_low_prior)
centers_low_prior = np.sqrt(radius_log_low_prior[1:] * radius_log_low_prior[:-1])
counts_low_prior = np.histogram(lateral_distance_copy_low_prior, bins=radius_log_low_prior)[0]
areas_log_low_prior = 2*np.pi*(radius_log_low_prior[1:]**2 - radius_log_low_prior[:-1]**2) 
LD_low_prior_out = [[centers_low_prior[i], (counts_low_prior[i] * areas_log_low_prior[i] / 3 * 507/700000000)] for i in range(LD_bin - 1)]

# Low Later
lateral_distance_copy_low_later = [x for x in lateral_distance_low_later if x <= 2500]
radius_log_low_later = np.logspace(np.log10(1), np.log10(2500), LD_bin)
logwidths_low_later = np.diff(radius_log_low_later)
centers_low_later = np.sqrt(radius_log_low_later[1:] * radius_log_low_later[:-1])
counts_low_later = np.histogram(lateral_distance_copy_low_later, bins=radius_log_low_later)[0]
areas_log_low_later = 2*np.pi*(radius_log_low_later[1:]**2 - radius_log_low_later[:-1]**2) 
LD_low_later_out = [[centers_low_later[i], (counts_low_later[i] * areas_log_low_later[i] / 3 * 507/700000000)] for i in range(LD_bin - 1)]


np.savez("/ceph/work/SATORI/projects/TA-ASIoP/sd_waveform/iron_mid.npz", 
up_arrival_out= up_arrival_out,
low_arrival_out = low_arrival_out,
LD_up_prior_out= LD_up_prior_out,
LD_up_later_out = LD_up_later_out,
LD_low_prior_out = LD_low_prior_out,
LD_low_later_out = LD_low_later_out
)

     

# import copy
# detector_area = 3
# density = 507/1000000


# lateral_distance_copy_up_prior = copy.deepcopy(lateral_distance_up_prior)
# lateral_distance_copy_up_prior = [x  for x in lateral_distance_copy_up_prior if x <= 2500]
# area_up_prior = []
# number_of_sd_up_prior = []

# radius_log_up_prior = np.logspace(np.log10(min(lateral_distance_copy_up_prior)), np.log10(max(lateral_distance_copy_up_prior)), 11)

# logwidths_up_prior = np.diff(radius_log_up_prior)
# centers_up_prior = np.sqrt(radius_log_up_prior[1:]*radius_log_up_prior[:-1])


# # counts_up_prior = np.histogram(lateral_distance_copy_up_prior, bins = radius_log_up_prior)[0]
# counts_up_prior = np.histogram(lateral_distance_copy_up_prior, bins = radius_log_up_prior)[0]
# areas_log_up_prior = np.pi*(radius_log_up_prior[1:]**2 - radius_log_up_prior[:-1]**2) * 3 * density
# # areas_log_up_prior = 2 * np.pi*(radius_log_up_prior[1:]**2 - radius_log_up_prior[:-1]**2) * 3 * density

# ################################################################################
# lateral_distance_copy_up_later = copy.deepcopy(lateral_distance_up_later)
# lateral_distance_copy_up_later = [x for x in lateral_distance_copy_up_later if x <= 2500]
# area_up_later = []
# number_of_sd_up_later = []

# radius_log_up_later = np.logspace(np.log10(min(lateral_distance_copy_up_later)), np.log10(max(lateral_distance_copy_up_later)), 11)
# logwidths_up_later = np.diff(radius_log_up_later)
# centers_up_later = np.sqrt(radius_log_up_later[1:] * radius_log_up_later[:-1])

# counts_up_later = np.histogram(lateral_distance_copy_up_later, bins=radius_log_up_later)[0]
# areas_log_up_later =  np.pi * (radius_log_up_later[1:]**2 - radius_log_up_later[:-1]**2) * 3 * density
# ################################################################################
# lateral_distance_copy_low_prior = copy.deepcopy(lateral_distance_low_prior)
# lateral_distance_copy_low_prior = [x for x in lateral_distance_copy_low_prior if x <= 2500]
# area_low_prior = []
# number_of_sd_low_prior = []

# radius_log_low_prior = np.logspace(np.log10(min(lateral_distance_copy_low_prior)), np.log10(max(lateral_distance_copy_low_prior)), 11)
# logwidths_low_prior = np.diff(radius_log_low_prior)
# centers_low_prior = np.sqrt(radius_log_low_prior[1:] * radius_log_low_prior[:-1])

# counts_low_prior = np.histogram(lateral_distance_copy_low_prior, bins=radius_log_low_prior)[0]
# areas_log_low_prior =  np.pi * (radius_log_low_prior[1:]**2 - radius_log_low_prior[:-1]**2) * detector_area * density
# ################################################################################
# lateral_distance_copy_low_later = copy.deepcopy(lateral_distance_low_later)
# lateral_distance_copy_low_later = [x  for x in lateral_distance_copy_low_later if x <= 2500]
# area_low_later = []
# number_of_sd_low_later = []

# radius_log_low_later = np.logspace(np.log10(min(lateral_distance_copy_low_later)), np.log10(max(lateral_distance_copy_low_later)), 11)
# logwidths_low_later = np.diff(radius_log_low_later)
# centers_low_later = np.sqrt(radius_log_low_later[1:] * radius_log_low_later[:-1])

# counts_low_later = np.histogram(lateral_distance_copy_low_later, bins=radius_log_low_later)[0]
# areas_log_low_later =  np.pi * (radius_log_low_later[1:]**2 - radius_log_low_later[:-1]**2) * detector_area * density

# plt.figure(figsize=(15, 15))
# plt.subplot(2, 2, 1)
# plt.errorbar(centers_up_prior, counts_up_prior,yerr= np.sqrt(counts_up_prior), fmt='rs')
# plt.xlabel('Lateral Distance (m)')
# plt.ylabel('Number of Events(count)')
# plt.title('Histogram of Up Uncorrelation Lateral Distances Prior to Separation Time')

# plt.subplot(2, 2, 2)
# plt.errorbar(centers_up_later, counts_up_later , yerr=np.sqrt(counts_up_later) , fmt='rs')
# plt.xlabel('Lateral Distance (m)')
# plt.ylabel('Number of Events(count)')
# plt.title('Histogram of Up Uncorrelation Lateral Distances Later Than Separation Time')

# plt.subplot(2, 2, 3)
# plt.errorbar(centers_low_prior, counts_low_prior, yerr=np.sqrt(counts_low_prior) , fmt='rs')
# plt.xlabel('Lateral Distance (m)')
# plt.ylabel('Number of Events(count)')
# plt.title('Histogram of Low Uncorrelation Lateral Distances Prior to Separation Time')

# plt.subplot(2, 2, 4)
# plt.errorbar(centers_low_later, counts_low_later , yerr=np.sqrt(counts_low_later) , fmt='rs')
# plt.xlabel('Lateral Distance (m)')
# plt.ylabel('Number of Events(count)')
# plt.title('Histogram of Low Uncorrelation Lateral Distances Later Than Separation Time')
# plt.savefig("Lateral_Distance_IRON_MID.png")
# plt.close()

# ################################################################################

# plt.figure(figsize=(15, 15))
# plt.subplot(2, 2, 1)
# plt.errorbar(centers_up_prior, counts_up_prior,yerr= np.sqrt(counts_up_prior), fmt='rs')
# plt.xlabel('Lateral Distance (m)')
# plt.ylabel('Number of Events(count)')
# plt.title('Histogram of Up Uncorrelation Lateral Distances Prior to Separation Time')
# plt.yscale("log")


# plt.subplot(2, 2, 2)
# plt.errorbar(centers_up_later, counts_up_later, yerr=np.sqrt(counts_up_later), fmt='rs')
# plt.xlabel('Lateral Distance (m)')
# plt.ylabel('Number of Events(count)')
# plt.title('Histogram of Up Uncorrelation Lateral Distances Later Than Separation Time')
# plt.yscale("log")

# plt.subplot(2, 2, 3)
# plt.errorbar(centers_low_prior, counts_low_prior, yerr=np.sqrt(counts_low_prior), fmt='rs')
# plt.xlabel('Lateral Distance (m)')
# plt.ylabel('Number of Events(count)')
# plt.title('Histogram of Low Uncorrelation Lateral Distances Prior to Separation Time, Normalized')
# plt.yscale("log")

# plt.subplot(2, 2, 4)
# plt.errorbar(centers_low_later, counts_low_later, yerr=np.sqrt(counts_low_later), fmt='rs')
# plt.xlabel('Lateral Distance (m)')
# plt.ylabel('Number of Events(count)')
# plt.title('Histogram of Low Uncorrelation Lateral Distances Later Than Separation Time, Normalized')
# plt.yscale("log")
# plt.savefig("Lateral_Distance_IRON_MID_LOG.png")
# plt.close()



