import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['figure.dpi'] = 400

sd_low_en = np.load("/ceph/work/SATORI/projects/TA-ASIoP/sd_waveform/sd_low.npz")
sd_mid_en = np.load("/ceph/work/SATORI/projects/TA-ASIoP/sd_waveform/sd_mid.npz")
sd_high_en = np.load("/ceph/work/SATORI/projects/TA-ASIoP/sd_waveform/sd_high.npz")
pro_low_en = np.load("/ceph/work/SATORI/projects/TA-ASIoP/sd_waveform/proton_low.npz")
pro_mid_en = np.load("/ceph/work/SATORI/projects/TA-ASIoP/sd_waveform/proton_mid.npz")
pro_high_en = np.load("/ceph/work/SATORI/projects/TA-ASIoP/sd_waveform/proton_high.npz")
iro_low_en = np.load("/ceph/work/SATORI/projects/TA-ASIoP/sd_waveform/iron_low.npz")
iro_mid_en = np.load("/ceph/work/SATORI/projects/TA-ASIoP/sd_waveform/iron_mid.npz")
iro_high_en = np.load("/ceph/work/SATORI/projects/TA-ASIoP/sd_waveform/iron_high.npz")

#####
sd_arr_lowen_up_arr = sd_low_en["up_arrival_out"]
sd_arr_lowen_low_arr= sd_low_en["low_arrival_out"]
sd_LD_lowen_up_prior = sd_low_en["LD_up_prior_out"]
sd_LD_lowen_up_later = sd_low_en["LD_up_later_out"]
sd_LD_lowen_low_prior = sd_low_en["LD_low_prior_out"]
sd_LD_lowen_low_later = sd_low_en["LD_low_later_out"]

sd_arr_miden_up_arr = sd_mid_en["up_arrival_out"]
sd_arr_miden_low_arr= sd_mid_en["low_arrival_out"]
sd_LD_miden_up_prior = sd_mid_en["LD_up_prior_out"]
sd_LD_miden_up_later = sd_mid_en["LD_up_later_out"]
sd_LD_miden_low_prior = sd_mid_en["LD_low_prior_out"]
sd_LD_miden_low_later = sd_mid_en["LD_low_later_out"]

sd_arr_highen_up_arr = sd_high_en["up_arrival_out"]
sd_arr_highen_low_arr= sd_high_en["low_arrival_out"]
sd_LD_highen_up_prior = sd_high_en["LD_up_prior_out"]
sd_LD_highen_up_later = sd_high_en["LD_up_later_out"]
sd_LD_highen_low_prior = sd_high_en["LD_low_prior_out"]
sd_LD_highen_low_later = sd_high_en["LD_low_later_out"]
######
pro_arr_lowen_up_arr = pro_low_en["up_arrival_out"]
pro_arr_lowen_low_arr= pro_low_en["low_arrival_out"]
pro_LD_lowen_up_prior = pro_low_en["LD_up_prior_out"]
pro_LD_lowen_up_later = pro_low_en["LD_up_later_out"]
pro_LD_lowen_low_prior = pro_low_en["LD_low_prior_out"]
pro_LD_lowen_low_later = pro_low_en["LD_low_later_out"]

pro_arr_miden_up_arr = pro_mid_en["up_arrival_out"]
pro_arr_miden_low_arr= pro_mid_en["low_arrival_out"]
pro_LD_miden_up_prior = pro_mid_en["LD_up_prior_out"]
pro_LD_miden_up_later = pro_mid_en["LD_up_later_out"]
pro_LD_miden_low_prior = pro_mid_en["LD_low_prior_out"]
pro_LD_miden_low_later = pro_mid_en["LD_low_later_out"]

pro_arr_highen_up_arr = pro_high_en["up_arrival_out"]
pro_arr_highen_low_arr= pro_high_en["low_arrival_out"]
pro_LD_highen_up_prior = pro_high_en["LD_up_prior_out"]
pro_LD_highen_up_later = pro_high_en["LD_up_later_out"]
pro_LD_highen_low_prior = pro_high_en["LD_low_prior_out"]
pro_LD_highen_low_later = pro_high_en["LD_low_later_out"]
######
iro_arr_lowen_up_arr = iro_low_en["up_arrival_out"]
iro_arr_lowen_low_arr= iro_low_en["low_arrival_out"]
iro_LD_lowen_up_prior = iro_low_en["LD_up_prior_out"]
iro_LD_lowen_up_later = iro_low_en["LD_up_later_out"]
iro_LD_lowen_low_prior = iro_low_en["LD_low_prior_out"]
iro_LD_lowen_low_later = iro_low_en["LD_low_later_out"]

iro_arr_miden_up_arr = iro_mid_en["up_arrival_out"]
iro_arr_miden_low_arr= iro_mid_en["low_arrival_out"]
iro_LD_miden_up_prior = iro_mid_en["LD_up_prior_out"]
iro_LD_miden_up_later = iro_mid_en["LD_up_later_out"]
iro_LD_miden_low_prior = iro_mid_en["LD_low_prior_out"]
iro_LD_miden_low_later = iro_mid_en["LD_low_later_out"]

iro_arr_highen_up_arr = iro_high_en["up_arrival_out"]
iro_arr_highen_low_arr= iro_high_en["low_arrival_out"]
iro_LD_highen_up_prior = iro_high_en["LD_up_prior_out"]
iro_LD_highen_up_later = iro_high_en["LD_up_later_out"]
iro_LD_highen_low_prior = iro_high_en["LD_low_prior_out"]
iro_LD_highen_low_later = iro_high_en["LD_low_later_out"]
###################
####Upper
fig, ax = plt.subplots(1, 2, figsize=(12, 8))
#TA SD
x = sd_arr_lowen_up_arr[:, 0]
yobs_up = [int(i) for i in sd_arr_lowen_up_arr[:, 1]]
ax[0].errorbar(x,
               yobs_up,
               yerr = np.sqrt(yobs_up),
               fmt = "o",
               color = "k",
               label = "Observation")

#Proton
x = pro_arr_lowen_up_arr[:, 0]
x_step = np.hstack([np.hstack([x[0]-(x[1]-x[0]), x]), x[-1]+(x[-1]-x[-2])])
y = [int(i) for i in pro_arr_lowen_up_arr[:, 1]]
y_step = np.hstack([np.hstack([0, y]), 0])
norm_to_obsenum = np.sum(yobs_up) / np.sum(y)
ax[0].errorbar(x,
               yobs_up,
               yerr = np.sqrt(yobs_up),
               fmt = "mid",
               color = "red",
               label = r"Proton MC")
#Iron 
x = iro_arr_lowen_up_arr[:, 0]
x_step = np.hstack([np.hstack([x[0]-(x[1]-x[0]), x]), x[-1]+(x[-1]-x[-2])])
yobs_up = [int(i) for i in iro_arr_lowen_up_arr[:, 1]]
y_step = np.hstack([np.hstack([0, y]), 0])
norm_to_obsenum = np.sum(yobs_up) / np.sum(y)
ax[0].errorbar(x,
               yobs_up,
               yerr = np.sqrt(yobs_up),
               fmt = "mid",
               color = "blue",
               label = r"Iron MC")
ax[0].set_title("Upper Layer")


###Lower
#TA SD
x = sd_arr_lowen_low_arr[:, 0]
yobs_up = [int(i) for i in sd_arr_lowen_low_arr[:, 1]]
ax[1].errorbar(x,
               yobs_up,
               yerr = np.sqrt(yobs_up),
               fmt = "o",
               color = "k",
               label = "Observation")

##Proton
x = pro_arr_lowen_low_arr[:, 0]
x_step = np.hstack([np.hstack([x[0]-(x[1]-x[0]), x]), x[-1]+(x[-1]-x[-2])])
y = [int(i) for i in pro_arr_lowen_low_arr[:, 1]]
y_step = np.hstack([np.hstack([0, y]), 0])
norm_to_obsenum = np.sum(yobs_up) / np.sum(y)
ax[1].errorbar(x,
               yobs_up,
               yerr = np.sqrt(yobs_up),
               fmt = "mid",
               color = "red",
               label = r"Proton MC")
##Iron 
x = iro_arr_lowen_low_arr[:, 0]
x_step = np.hstack([np.hstack([x[0]-(x[1]-x[0]), x]), x[-1]+(x[-1]-x[-2])])
yobs_up = [int(i) for i in iro_arr_lowen_low_arr[:, 1]]
y_step = np.hstack([np.hstack([0, y]), 0])
norm_to_obsenum = np.sum(yobs_up) / np.sum(y)
ax[1].errorbar(x,
               yobs_up,
               yerr = np.sqrt(yobs_up),
               fmt = "mid",
               color = "blue",
               label = r"Iron MC")
ax[1].set_title("Lower Layer")

for ax in ax:
    ax.set_yscale("log")
    ax.set_xlabel(r"Time [$\mu{\rm s}$]")
    ax.set_ylabel("Normalized number of events")
    ax.set_xticks(np.linspace(0, 12, 13))
    ax.set_xlim(0, 6)
    ax.set_ylim(50, 50000)
    ax.legend()
#############
####Upper
fig, ax = plt.subplots(1, 2, figsize=(12, 8))
#TA SD
x = sd_arr_miden_up_arr[:, 0]
yobs_up = [int(i) for i in sd_arr_miden_up_arr[:, 1]]
ax[0].errorbar(x,
               yobs_up,
               yerr = np.sqrt(yobs_up),
               fmt = "o",
               color = "k",
               label = "Observation")

#Proton
x = pro_arr_miden_up_arr[:, 0]
x_step = np.hstack([np.hstack([x[0]-(x[1]-x[0]), x]), x[-1]+(x[-1]-x[-2])])
y = [int(i) for i in pro_arr_miden_up_arr[:, 1]]
y_step = np.hstack([np.hstack([0, y]), 0])
norm_to_obsenum = np.sum(yobs_up) / np.sum(y)
ax[0].errorbar(x,
               yobs_up,
               yerr = np.sqrt(yobs_up),
               fmt = "mid",
               color = "red",
               label = r"Proton MC")
#Iron 
x = iro_arr_miden_up_arr[:, 0]
x_step = np.hstack([np.hstack([x[0]-(x[1]-x[0]), x]), x[-1]+(x[-1]-x[-2])])
yobs_up = [int(i) for i in iro_arr_miden_up_arr[:, 1]]
y_step = np.hstack([np.hstack([0, y]), 0])
norm_to_obsenum = np.sum(yobs_up) / np.sum(y)
ax[0].errorbar(x,
               yobs_up,
               yerr = np.sqrt(yobs_up),
               fmt = "mid",
               color = "blue",
               label = r"Iron MC")
ax[0].set_title("Upper Layer")


###Lower
#TA SD
x = sd_arr_miden_low_arr[:, 0]
yobs_up = [int(i) for i in sd_arr_miden_low_arr[:, 1]]
ax[1].errorbar(x,
               yobs_up,
               yerr = np.sqrt(yobs_up),
               fmt = "o",
               color = "k",
               label = "Observation")

##Proton
x = pro_arr_miden_low_arr[:, 0]
x_step = np.hstack([np.hstack([x[0]-(x[1]-x[0]), x]), x[-1]+(x[-1]-x[-2])])
y = [int(i) for i in pro_arr_miden_low_arr[:, 1]]
y_step = np.hstack([np.hstack([0, y]), 0])
norm_to_obsenum = np.sum(yobs_up) / np.sum(y)
ax[1].errorbar(x,
               yobs_up,
               yerr = np.sqrt(yobs_up),
               fmt = "mid",
               color = "red",
               label = r"Proton MC")
##Iron 
x = iro_arr_miden_low_arr[:, 0]
x_step = np.hstack([np.hstack([x[0]-(x[1]-x[0]), x]), x[-1]+(x[-1]-x[-2])])
yobs_up = [int(i) for i in iro_arr_miden_low_arr[:, 1]]
y_step = np.hstack([np.hstack([0, y]), 0])
norm_to_obsenum = np.sum(yobs_up) / np.sum(y)
ax[1].errorbar(x,
               yobs_up,
               yerr = np.sqrt(yobs_up),
               fmt = "mid",
               color = "blue",
               label = r"Iron MC")
ax[1].set_title("Lower Layer")

for ax in ax:
    ax.set_yscale("log")
    ax.set_xlabel(r"Time [$\mu{\rm s}$]")
    ax.set_ylabel("Normalized number of events")
    ax.set_xticks(np.linspace(0, 12, 13))
    ax.set_xlim(0, 6)
    ax.set_ylim(50, 50000)
    ax.legend()
###############
####Upper
fig, ax = plt.subplots(1, 2, figsize=(12, 8))
#TA SD
x = sd_arr_highen_up_arr[:, 0]
yobs_up = [int(i) for i in sd_arr_highen_up_arr[:, 1]]
ax[0].errorbar(x,
               yobs_up,
               yerr = np.sqrt(yobs_up),
               fmt = "o",
               color = "k",
               label = "Observation")

#Proton
x = pro_arr_highen_up_arr[:, 0]
x_step = np.hstack([np.hstack([x[0]-(x[1]-x[0]), x]), x[-1]+(x[-1]-x[-2])])
y = [int(i) for i in pro_arr_highen_up_arr[:, 1]]
y_step = np.hstack([np.hstack([0, y]), 0])
norm_to_obsenum = np.sum(yobs_up) / np.sum(y)
ax[0].errorbar(x,
               yobs_up,
               yerr = np.sqrt(yobs_up),
               fmt = "mid",
               color = "red",
               label = r"Proton MC")
#Iron 
x = iro_arr_highen_up_arr[:, 0]
x_step = np.hstack([np.hstack([x[0]-(x[1]-x[0]), x]), x[-1]+(x[-1]-x[-2])])
yobs_up = [int(i) for i in iro_arr_highen_up_arr[:, 1]]
y_step = np.hstack([np.hstack([0, y]), 0])
norm_to_obsenum = np.sum(yobs_up) / np.sum(y)
ax[0].errorbar(x,
               yobs_up,
               yerr = np.sqrt(yobs_up),
               fmt = "mid",
               color = "blue",
               label = r"Iron MC")
ax[0].set_title("Upper Layer")


###Lower
#TA SD
x = sd_arr_highen_low_arr[:, 0]
yobs_up = [int(i) for i in sd_arr_highen_low_arr[:, 1]]
ax[1].errorbar(x,
               yobs_up,
               yerr = np.sqrt(yobs_up),
               fmt = "o",
               color = "k",
               label = "Observation")

##Proton
x = pro_arr_highen_low_arr[:, 0]
x_step = np.hstack([np.hstack([x[0]-(x[1]-x[0]), x]), x[-1]+(x[-1]-x[-2])])
y = [int(i) for i in pro_arr_highen_low_arr[:, 1]]
y_step = np.hstack([np.hstack([0, y]), 0])
norm_to_obsenum = np.sum(yobs_up) / np.sum(y)
ax[1].errorbar(x,
               yobs_up,
               yerr = np.sqrt(yobs_up),
               fmt = "mid",
               color = "red",
               label = r"Proton MC")
##Iron 
x = iro_arr_highen_low_arr[:, 0]
x_step = np.hstack([np.hstack([x[0]-(x[1]-x[0]), x]), x[-1]+(x[-1]-x[-2])])
yobs_up = [int(i) for i in iro_arr_highen_low_arr[:, 1]]
y_step = np.hstack([np.hstack([0, y]), 0])
norm_to_obsenum = np.sum(yobs_up) / np.sum(y)
ax[1].errorbar(x,
               yobs_up,
               yerr = np.sqrt(yobs_up),
               fmt = "mid",
               color = "blue",
               label = r"Iron MC")
ax[1].set_title("Lower Layer")

for ax in ax:
    ax.set_yscale("log")
    ax.set_xlabel(r"Time [$\mu{\rm s}$]")
    ax.set_ylabel("Normalized number of events")
    ax.set_xticks(np.linspace(0, 12, 13))
    ax.set_xlim(0, 6)
    ax.set_ylim(50, 50000)
    ax.legend()
###################
####Upper
fig, ax = plt.subplots(1, 2, figsize=(12, 8))
#TA SD
x = sd_LD_lowen_up_prior[:, 0]
yobs_up = [int(i) for i in sd_LD_lowen_up_prior[:, 1]]
ax[0].errorbar(x,
               yobs_up,
               yerr = np.sqrt(yobs_up),
               fmt = "o",
               color = "k",
               label = "Observation")

#Proton
x = pro_LD_lowen_up_prior[:, 0]
x_step = np.hstack([np.hstack([x[0]-(x[1]-x[0]), x]), x[-1]+(x[-1]-x[-2])])
y = [int(i) for i in pro_LD_lowen_up_prior[:, 1]]
y_step = np.hstack([np.hstack([0, y]), 0])
norm_to_obsenum = np.sum(yobs_up) / np.sum(y)
ax[0].errorbar(x,
               yobs_up,
               yerr = np.sqrt(yobs_up),
               fmt = "mid",
               color = "red",
               label = r"Proton MC")
#Iron 
x = iro_LD_lowen_up_prior[:, 0]
x_step = np.hstack([np.hstack([x[0]-(x[1]-x[0]), x]), x[-1]+(x[-1]-x[-2])])
yobs_up = [int(i) for i in iro_LD_lowen_up_prior[:, 1]]
y_step = np.hstack([np.hstack([0, y]), 0])
norm_to_obsenum = np.sum(yobs_up) / np.sum(y)
ax[0].errorbar(x,
               yobs_up,
               yerr = np.sqrt(yobs_up),
               fmt = "mid",
               color = "blue",
               label = r"Iron MC")
ax[0].set_title("Upper Layer")


###Lower
#TA SD
x = sd_LD_lowen_low_prior[:, 0]
yobs_up = [int(i) for i in sd_LD_lowen_low_prior[:, 1]]
ax[1].errorbar(x,
               yobs_up,
               yerr = np.sqrt(yobs_up),
               fmt = "o",
               color = "k",
               label = "Observation")

##Proton
x = pro_LD_lowen_low_prior[:, 0]
x_step = np.hstack([np.hstack([x[0]-(x[1]-x[0]), x]), x[-1]+(x[-1]-x[-2])])
y = [int(i) for i in pro_LD_lowen_low_prior[:, 1]]
y_step = np.hstack([np.hstack([0, y]), 0])
norm_to_obsenum = np.sum(yobs_up) / np.sum(y)
ax[1].errorbar(x,
               yobs_up,
               yerr = np.sqrt(yobs_up),
               fmt = "mid",
               color = "red",
               label = r"Proton MC")
##Iron 
x = iro_LD_lowen_low_prior[:, 0]
x_step = np.hstack([np.hstack([x[0]-(x[1]-x[0]), x]), x[-1]+(x[-1]-x[-2])])
yobs_up = [int(i) for i in iro_LD_lowen_low_prior[:, 1]]
y_step = np.hstack([np.hstack([0, y]), 0])
norm_to_obsenum = np.sum(yobs_up) / np.sum(y)
ax[1].errorbar(x,
               yobs_up,
               yerr = np.sqrt(yobs_up),
               fmt = "mid",
               color = "blue",
               label = r"Iron MC")
ax[1].set_title("Lower Layer")

for ax in ax:
    ax.set_yscale("log")
    ax.set_xlabel(r"Lateral Listance [m]]")
    ax.set_ylabel("Normalized number of events")
    ax.set_xticks(np.arange(0, 2501, 250))
    ax.set_xlim(0, 2500)
    ax.set_ylim(50, 50000)
    ax.legend()
#################
####Upper
fig, ax = plt.subplots(1, 2, figsize=(12, 8))
#TA SD
x = sd_LD_lowen_up_later[:, 0]
yobs_up = [int(i) for i in sd_LD_lowen_up_later[:, 1]]
ax[0].errorbar(x,
               yobs_up,
               yerr = np.sqrt(yobs_up),
               fmt = "o",
               color = "k",
               label = "Observation")

#Proton
x = pro_LD_lowen_up_later[:, 0]
x_step = np.hstack([np.hstack([x[0]-(x[1]-x[0]), x]), x[-1]+(x[-1]-x[-2])])
y = [int(i) for i in pro_LD_lowen_up_later[:, 1]]
y_step = np.hstack([np.hstack([0, y]), 0])
norm_to_obsenum = np.sum(yobs_up) / np.sum(y)
ax[0].errorbar(x,
               yobs_up,
               yerr = np.sqrt(yobs_up),
               fmt = "mid",
               color = "red",
               label = r"Proton MC")
#Iron 
x = iro_LD_lowen_up_later[:, 0]
x_step = np.hstack([np.hstack([x[0]-(x[1]-x[0]), x]), x[-1]+(x[-1]-x[-2])])
yobs_up = [int(i) for i in iro_LD_lowen_up_later[:, 1]]
y_step = np.hstack([np.hstack([0, y]), 0])
norm_to_obsenum = np.sum(yobs_up) / np.sum(y)
ax[0].errorbar(x,
               yobs_up,
               yerr = np.sqrt(yobs_up),
               fmt = "mid",
               color = "blue",
               label = r"Iron MC")
ax[0].set_title("Upper Layer")


###Lower
#TA SD
x = sd_LD_lowen_low_later[:, 0]
yobs_up = [int(i) for i in sd_LD_lowen_low_later[:, 1]]
ax[1].errorbar(x,
               yobs_up,
               yerr = np.sqrt(yobs_up),
               fmt = "o",
               color = "k",
               label = "Observation")

##Proton
x = pro_LD_lowen_low_later[:, 0]
x_step = np.hstack([np.hstack([x[0]-(x[1]-x[0]), x]), x[-1]+(x[-1]-x[-2])])
y = [int(i) for i in pro_LD_lowen_low_later[:, 1]]
y_step = np.hstack([np.hstack([0, y]), 0])
norm_to_obsenum = np.sum(yobs_up) / np.sum(y)
ax[1].errorbar(x,
               yobs_up,
               yerr = np.sqrt(yobs_up),
               fmt = "mid",
               color = "red",
               label = r"Proton MC")
##Iron 
x = iro_LD_lowen_low_later[:, 0]
x_step = np.hstack([np.hstack([x[0]-(x[1]-x[0]), x]), x[-1]+(x[-1]-x[-2])])
yobs_up = [int(i) for i in iro_LD_lowen_low_later[:, 1]]
y_step = np.hstack([np.hstack([0, y]), 0])
norm_to_obsenum = np.sum(yobs_up) / np.sum(y)
ax[1].errorbar(x,
               yobs_up,
               yerr = np.sqrt(yobs_up),
               fmt = "mid",
               color = "blue",
               label = r"Iron MC")
ax[1].set_title("Lower Layer")

for ax in ax:
    ax.set_yscale("log")
    ax.set_xlabel(r"Lateral Listance [m]]")
    ax.set_ylabel("Normalized number of events")
    ax.set_xticks(np.arange(0, 2501, 250))
    ax.set_xlim(0, 2500)
    ax.set_ylim(50, 50000)
    ax.legend()
#################
####Upper
fig, ax = plt.subplots(1, 2, figsize=(12, 8))
#TA SD
x = sd_LD_miden_up_prior[:, 0]
yobs_up = [int(i) for i in sd_LD_miden_up_prior[:, 1]]
ax[0].errorbar(x,
               yobs_up,
               yerr = np.sqrt(yobs_up),
               fmt = "o",
               color = "k",
               label = "Observation")

#Proton
x = pro_LD_miden_up_prior[:, 0]
x_step = np.hstack([np.hstack([x[0]-(x[1]-x[0]), x]), x[-1]+(x[-1]-x[-2])])
y = [int(i) for i in pro_LD_miden_up_prior[:, 1]]
y_step = np.hstack([np.hstack([0, y]), 0])
norm_to_obsenum = np.sum(yobs_up) / np.sum(y)
ax[0].errorbar(x,
               yobs_up,
               yerr = np.sqrt(yobs_up),
               fmt = "mid",
               color = "red",
               label = r"Proton MC")
#Iron 
x = iro_LD_miden_up_prior[:, 0]
x_step = np.hstack([np.hstack([x[0]-(x[1]-x[0]), x]), x[-1]+(x[-1]-x[-2])])
yobs_up = [int(i) for i in iro_LD_miden_up_prior[:, 1]]
y_step = np.hstack([np.hstack([0, y]), 0])
norm_to_obsenum = np.sum(yobs_up) / np.sum(y)
ax[0].errorbar(x,
               yobs_up,
               yerr = np.sqrt(yobs_up),
               fmt = "mid",
               color = "blue",
               label = r"Iron MC")
ax[0].set_title("Upper Layer")


###Lower
#TA SD
x = sd_LD_miden_low_prior[:, 0]
yobs_up = [int(i) for i in sd_LD_miden_low_prior[:, 1]]
ax[1].errorbar(x,
               yobs_up,
               yerr = np.sqrt(yobs_up),
               fmt = "o",
               color = "k",
               label = "Observation")

##Proton
x = pro_LD_miden_low_prior[:, 0]
x_step = np.hstack([np.hstack([x[0]-(x[1]-x[0]), x]), x[-1]+(x[-1]-x[-2])])
y = [int(i) for i in pro_LD_miden_low_prior[:, 1]]
y_step = np.hstack([np.hstack([0, y]), 0])
norm_to_obsenum = np.sum(yobs_up) / np.sum(y)
ax[1].errorbar(x,
               yobs_up,
               yerr = np.sqrt(yobs_up),
               fmt = "mid",
               color = "red",
               label = r"Proton MC")
##Iron 
x = iro_LD_miden_low_prior[:, 0]
x_step = np.hstack([np.hstack([x[0]-(x[1]-x[0]), x]), x[-1]+(x[-1]-x[-2])])
yobs_up = [int(i) for i in iro_LD_miden_low_prior[:, 1]]
y_step = np.hstack([np.hstack([0, y]), 0])
norm_to_obsenum = np.sum(yobs_up) / np.sum(y)
ax[1].errorbar(x,
               yobs_up,
               yerr = np.sqrt(yobs_up),
               fmt = "mid",
               color = "blue",
               label = r"Iron MC")
ax[1].set_title("Lower Layer")

for ax in ax:
    ax.set_yscale("log")
    ax.set_xlabel(r"Lateral Listance [m]]")
    ax.set_ylabel("Normalized number of events")
    ax.set_xticks(np.arange(0, 2501, 250))
    ax.set_xlim(0, 2500)
    ax.set_ylim(50, 50000)
    ax.legend()
################
####Upper
fig, ax = plt.subplots(1, 2, figsize=(12, 8))
#TA SD
x = sd_LD_miden_up_later[:, 0]
yobs_up = [int(i) for i in sd_LD_miden_up_later[:, 1]]
ax[0].errorbar(x,
               yobs_up,
               yerr = np.sqrt(yobs_up),
               fmt = "o",
               color = "k",
               label = "Observation")

#Proton
x = pro_LD_miden_up_later[:, 0]
x_step = np.hstack([np.hstack([x[0]-(x[1]-x[0]), x]), x[-1]+(x[-1]-x[-2])])
y = [int(i) for i in pro_LD_miden_up_later[:, 1]]
y_step = np.hstack([np.hstack([0, y]), 0])
norm_to_obsenum = np.sum(yobs_up) / np.sum(y)
ax[0].errorbar(x,
               yobs_up,
               yerr = np.sqrt(yobs_up),
               fmt = "mid",
               color = "red",
               label = r"Proton MC")
#Iron 
x = iro_LD_miden_up_later[:, 0]
x_step = np.hstack([np.hstack([x[0]-(x[1]-x[0]), x]), x[-1]+(x[-1]-x[-2])])
yobs_up = [int(i) for i in iro_LD_miden_up_later[:, 1]]
y_step = np.hstack([np.hstack([0, y]), 0])
norm_to_obsenum = np.sum(yobs_up) / np.sum(y)
ax[0].errorbar(x,
               yobs_up,
               yerr = np.sqrt(yobs_up),
               fmt = "mid",
               color = "blue",
               label = r"Iron MC")
ax[0].set_title("Upper Layer")


###Lower
#TA SD
x = sd_LD_miden_low_later[:, 0]
yobs_up = [int(i) for i in sd_LD_miden_low_later[:, 1]]
ax[1].errorbar(x,
               yobs_up,
               yerr = np.sqrt(yobs_up),
               fmt = "o",
               color = "k",
               label = "Observation")

##Proton
x = pro_LD_miden_low_later[:, 0]
x_step = np.hstack([np.hstack([x[0]-(x[1]-x[0]), x]), x[-1]+(x[-1]-x[-2])])
y = [int(i) for i in pro_LD_miden_low_later[:, 1]]
y_step = np.hstack([np.hstack([0, y]), 0])
norm_to_obsenum = np.sum(yobs_up) / np.sum(y)
ax[1].errorbar(x,
               yobs_up,
               yerr = np.sqrt(yobs_up),
               fmt = "mid",
               color = "red",
               label = r"Proton MC")
##Iron 
x = iro_LD_miden_low_later[:, 0]
x_step = np.hstack([np.hstack([x[0]-(x[1]-x[0]), x]), x[-1]+(x[-1]-x[-2])])
yobs_up = [int(i) for i in iro_LD_miden_low_later[:, 1]]
y_step = np.hstack([np.hstack([0, y]), 0])
norm_to_obsenum = np.sum(yobs_up) / np.sum(y)
ax[1].errorbar(x,
               yobs_up,
               yerr = np.sqrt(yobs_up),
               fmt = "mid",
               color = "blue",
               label = r"Iron MC")
ax[1].set_title("Lower Layer")

for ax in ax:
    ax.set_yscale("log")
    ax.set_xlabel(r"Lateral Listance [m]]")
    ax.set_ylabel("Normalized number of events")
    ax.set_xticks(np.arange(0, 2501, 250))
    ax.set_xlim(0, 2500)
    ax.set_ylim(50, 50000)
    ax.legend()
##################
####Upper
fig, ax = plt.subplots(1, 2, figsize=(12, 8))
#TA SD
x = sd_LD_highen_up_prior[:, 0]
yobs_up = [int(i) for i in sd_LD_highen_up_prior[:, 1]]
ax[0].errorbar(x,
               yobs_up,
               yerr = np.sqrt(yobs_up),
               fmt = "o",
               color = "k",
               label = "Observation")

#Proton
x = pro_LD_highen_up_prior[:, 0]
x_step = np.hstack([np.hstack([x[0]-(x[1]-x[0]), x]), x[-1]+(x[-1]-x[-2])])
y = [int(i) for i in pro_LD_highen_up_prior[:, 1]]
y_step = np.hstack([np.hstack([0, y]), 0])
norm_to_obsenum = np.sum(yobs_up) / np.sum(y)
ax[0].errorbar(x,
               yobs_up,
               yerr = np.sqrt(yobs_up),
               fmt = "mid",
               color = "red",
               label = r"Proton MC")
#Iron 
x = iro_LD_highen_up_prior[:, 0]
x_step = np.hstack([np.hstack([x[0]-(x[1]-x[0]), x]), x[-1]+(x[-1]-x[-2])])
yobs_up = [int(i) for i in iro_LD_highen_up_prior[:, 1]]
y_step = np.hstack([np.hstack([0, y]), 0])
norm_to_obsenum = np.sum(yobs_up) / np.sum(y)
ax[0].errorbar(x,
               yobs_up,
               yerr = np.sqrt(yobs_up),
               fmt = "mid",
               color = "blue",
               label = r"Iron MC")
ax[0].set_title("Upper Layer")


###Lower
#TA SD
x = sd_LD_highen_low_prior[:, 0]
yobs_up = [int(i) for i in sd_LD_highen_low_prior[:, 1]]
ax[1].errorbar(x,
               yobs_up,
               yerr = np.sqrt(yobs_up),
               fmt = "o",
               color = "k",
               label = "Observation")

##Proton
x = pro_LD_highen_low_prior[:, 0]
x_step = np.hstack([np.hstack([x[0]-(x[1]-x[0]), x]), x[-1]+(x[-1]-x[-2])])
y = [int(i) for i in pro_LD_highen_low_prior[:, 1]]
y_step = np.hstack([np.hstack([0, y]), 0])
norm_to_obsenum = np.sum(yobs_up) / np.sum(y)
ax[1].errorbar(x,
               yobs_up,
               yerr = np.sqrt(yobs_up),
               fmt = "mid",
               color = "red",
               label = r"Proton MC")
##Iron 
x = iro_LD_highen_low_prior[:, 0]
x_step = np.hstack([np.hstack([x[0]-(x[1]-x[0]), x]), x[-1]+(x[-1]-x[-2])])
yobs_up = [int(i) for i in iro_LD_highen_low_prior[:, 1]]
y_step = np.hstack([np.hstack([0, y]), 0])
norm_to_obsenum = np.sum(yobs_up) / np.sum(y)
ax[1].errorbar(x,
               yobs_up,
               yerr = np.sqrt(yobs_up),
               fmt = "mid",
               color = "blue",
               label = r"Iron MC")
ax[1].set_title("Lower Layer")

for ax in ax:
    ax.set_yscale("log")
    ax.set_xlabel(r"Lateral Listance [m]]")
    ax.set_ylabel("Normalized number of events")
    ax.set_xticks(np.arange(0, 2501, 250))
    ax.set_xlim(0, 2500)
    ax.set_ylim(50, 50000)
    ax.legend()
##################
####Upper
fig, ax = plt.subplots(1, 2, figsize=(12, 8))
#TA SD
x = sd_LD_highen_up_later[:, 0]
yobs_up = [int(i) for i in sd_LD_highen_up_later[:, 1]]
ax[0].errorbar(x,
               yobs_up,
               yerr = np.sqrt(yobs_up),
               fmt = "o",
               color = "k",
               label = "Observation")

#Proton
x = pro_LD_highen_up_later[:, 0]
x_step = np.hstack([np.hstack([x[0]-(x[1]-x[0]), x]), x[-1]+(x[-1]-x[-2])])
y = [int(i) for i in pro_LD_highen_up_later[:, 1]]
y_step = np.hstack([np.hstack([0, y]), 0])
norm_to_obsenum = np.sum(yobs_up) / np.sum(y)
ax[0].errorbar(x,
               yobs_up,
               yerr = np.sqrt(yobs_up),
               fmt = "mid",
               color = "red",
               label = r"Proton MC")
#Iron 
x = iro_LD_highen_up_later[:, 0]
x_step = np.hstack([np.hstack([x[0]-(x[1]-x[0]), x]), x[-1]+(x[-1]-x[-2])])
yobs_up = [int(i) for i in iro_LD_highen_up_later[:, 1]]
y_step = np.hstack([np.hstack([0, y]), 0])
norm_to_obsenum = np.sum(yobs_up) / np.sum(y)
ax[0].errorbar(x,
               yobs_up,
               yerr = np.sqrt(yobs_up),
               fmt = "mid",
               color = "blue",
               label = r"Iron MC")
ax[0].set_title("Upper Layer")


###Lower
#TA SD
x = sd_LD_highen_low_later[:, 0]
yobs_up = [int(i) for i in sd_LD_highen_low_later[:, 1]]
ax[1].errorbar(x,
               yobs_up,
               yerr = np.sqrt(yobs_up),
               fmt = "o",
               color = "k",
               label = "Observation")

##Proton
x = pro_LD_highen_low_later[:, 0]
x_step = np.hstack([np.hstack([x[0]-(x[1]-x[0]), x]), x[-1]+(x[-1]-x[-2])])
y = [int(i) for i in pro_LD_highen_low_later[:, 1]]
y_step = np.hstack([np.hstack([0, y]), 0])
norm_to_obsenum = np.sum(yobs_up) / np.sum(y)
ax[1].errorbar(x,
               yobs_up,
               yerr = np.sqrt(yobs_up),
               fmt = "mid",
               color = "red",
               label = r"Proton MC")
##Iron 
x = iro_LD_highen_low_later[:, 0]
x_step = np.hstack([np.hstack([x[0]-(x[1]-x[0]), x]), x[-1]+(x[-1]-x[-2])])
yobs_up = [int(i) for i in iro_LD_highen_low_later[:, 1]]
y_step = np.hstack([np.hstack([0, y]), 0])
norm_to_obsenum = np.sum(yobs_up) / np.sum(y)
ax[1].errorbar(x,
               yobs_up,
               yerr = np.sqrt(yobs_up),
               fmt = "mid",
               color = "blue",
               label = r"Iron MC")
ax[1].set_title("Lower Layer")

for ax in ax:
    ax.set_yscale("log")
    ax.set_xlabel(r"Lateral Listance [m]]")
    ax.set_ylabel("Normalized number of events")
    ax.set_xticks(np.arange(0, 2501, 250))
    ax.set_xlim(0, 2500)
    ax.set_ylim(50, 50000)
    ax.legend()
