from dstparser.dst_adapter import parse_dst_file_no_tiling
# from dstparser.tasd_clf import tasdmc_clf
from event_display import waveforms, footprint
import numpy as np
import matplotlib.pyplot as plt

### Amaterasu particle: YYMMDD = "210527", index = 183
# YYMMDD = "150423"
YYMMDD = "210527"
# "000125"
# YYMMDD = "080625"
dst_file = "/ceph/work/SATORI/projects/TA-ASIoP/tasdobs_dstbank/rufldf/tasdcalibev_pass2_%s.bsdinfo.rufldf.dst.gz"%(YYMMDD)
#dst_file = "/ceph/work/SATORI/projects/TA-ASIoP/tasdmc_dstbank/qgsii04proton/080417_160603/Em1_bsdinfo/DAT%s_gea.rufldf.dst.gz"%(YYMMDD)
data = parse_dst_file_no_tiling(dst_file)

data.keys()
index = np.where((data["std_recon"]["energy"] > 10) & (data["std_recon"]["nstclust"] > 5))[0]

# # print((data["signal_ixy"][index[0]]))
# # print(data["wf_ixy"][index[0]])

# index

isgood_option = "nstclust" ## showing shower-related signals
# isgood_option = False ## showing all signals
import matplotlib.pyplot as plt
plt.rcParams['figure.dpi'] = 150
fig, ax, colors, sdid_colors = footprint(data,
                                        index=index[0], 
                                        isgood_option = isgood_option)
fig, ax, sd_wf, sd_id = waveforms(data,
                                index = index[0],
                                colors = colors,
                                sdid_colors = sdid_colors,
                                with_start_time = False, 
                                isgood_option = isgood_option)

#fig

for ax_ in ax:
        ax_.set_xlim(0,
                     5)
fig
