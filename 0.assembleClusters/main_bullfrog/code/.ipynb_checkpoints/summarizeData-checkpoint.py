{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 23,
   "metadata": {},
   "outputs": [],
   "source": [
    "import ipyrad as ip\n",
    "import sys\n",
    "import os\n",
    "import pandas\n",
    "from os.path import join"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {},
   "outputs": [],
   "source": [
    "workDir=\"/home/nbe4/scratch60/0.assembleClusters/\"\n",
    "workDir=sys.argv[1]\n",
    "outDir=sys.argv[2]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "loading Assembly: myersPopGen_10000_09_05\n",
      "from saved path: /gpfs/loomis/scratch60/skelly/nbe4/0.assembleClusters/myersPopGen_10000_09_05.json\n",
      "loading Assembly: myersPopGen_100_09_035\n",
      "from saved path: /gpfs/loomis/scratch60/skelly/nbe4/0.assembleClusters/myersPopGen_100_09_035.json\n",
      "loading Assembly: myersPopGen_25_085_05\n",
      "from saved path: /gpfs/loomis/scratch60/skelly/nbe4/0.assembleClusters/myersPopGen_25_085_05.json\n",
      "loading Assembly: myersPopGen_100_085_02\n",
      "from saved path: /gpfs/loomis/scratch60/skelly/nbe4/0.assembleClusters/myersPopGen_100_085_02.json\n",
      "loading Assembly: myersPopGen_100_095_02\n",
      "from saved path: /gpfs/loomis/scratch60/skelly/nbe4/0.assembleClusters/myersPopGen_100_095_02.json\n",
      "loading Assembly: myersPopGen_25_085_035\n",
      "from saved path: /gpfs/loomis/scratch60/skelly/nbe4/0.assembleClusters/myersPopGen_25_085_035.json\n",
      "loading Assembly: myersPopGen_25_09_02\n",
      "from saved path: /gpfs/loomis/scratch60/skelly/nbe4/0.assembleClusters/myersPopGen_25_09_02.json\n",
      "loading Assembly: myersPopGen_10000_095_02\n",
      "from saved path: /gpfs/loomis/scratch60/skelly/nbe4/0.assembleClusters/myersPopGen_10000_095_02.json\n",
      "loading Assembly: myersPopGen_25_095_035\n",
      "from saved path: /gpfs/loomis/scratch60/skelly/nbe4/0.assembleClusters/myersPopGen_25_095_035.json\n",
      "loading Assembly: myersPopGen_10000_09_035\n",
      "from saved path: /gpfs/loomis/scratch60/skelly/nbe4/0.assembleClusters/myersPopGen_10000_09_035.json\n",
      "loading Assembly: myersPopGen_10000_085_05\n",
      "from saved path: /gpfs/loomis/scratch60/skelly/nbe4/0.assembleClusters/myersPopGen_10000_085_05.json\n",
      "loading Assembly: myersPopGen_50_09_05\n",
      "from saved path: /gpfs/loomis/scratch60/skelly/nbe4/0.assembleClusters/myersPopGen_50_09_05.json\n",
      "loading Assembly: myersPopGen_100_09_05\n",
      "from saved path: /gpfs/loomis/scratch60/skelly/nbe4/0.assembleClusters/myersPopGen_100_09_05.json\n",
      "loading Assembly: myersPopGen\n",
      "from saved path: /gpfs/loomis/project/skelly/nbe4/myersPopStructure/0.assembleClusters/myersPopGen.json\n",
      "loading Assembly: myersPopGen_50_09_02\n",
      "from saved path: /gpfs/loomis/scratch60/skelly/nbe4/0.assembleClusters/myersPopGen_50_09_02.json\n",
      "loading Assembly: myersPopGen_50_095_035\n",
      "from saved path: /gpfs/loomis/scratch60/skelly/nbe4/0.assembleClusters/myersPopGen_50_095_035.json\n",
      "loading Assembly: myersPopGen_10000_085_02\n",
      "from saved path: /gpfs/loomis/scratch60/skelly/nbe4/0.assembleClusters/myersPopGen_10000_085_02.json\n",
      "loading Assembly: myersPopGen_10000_09_02\n",
      "from saved path: /gpfs/loomis/scratch60/skelly/nbe4/0.assembleClusters/myersPopGen_10000_09_02.json\n",
      "loading Assembly: myersPopGen_10000_095_035\n",
      "from saved path: /gpfs/loomis/scratch60/skelly/nbe4/0.assembleClusters/myersPopGen_10000_095_035.json\n",
      "loading Assembly: myersPopGen_100_095_05\n",
      "from saved path: /gpfs/loomis/scratch60/skelly/nbe4/0.assembleClusters/myersPopGen_100_095_05.json\n",
      "loading Assembly: myersPopGen_25_095_02\n",
      "from saved path: /gpfs/loomis/scratch60/skelly/nbe4/0.assembleClusters/myersPopGen_25_095_02.json\n",
      "loading Assembly: myersPopGen_50_09_035\n",
      "from saved path: /gpfs/loomis/scratch60/skelly/nbe4/0.assembleClusters/myersPopGen_50_09_035.json\n",
      "loading Assembly: myersPopGen_10000_085_035\n",
      "from saved path: /gpfs/loomis/scratch60/skelly/nbe4/0.assembleClusters/myersPopGen_10000_085_035.json\n",
      "loading Assembly: myersPopGen_100_085_05\n",
      "from saved path: /gpfs/loomis/scratch60/skelly/nbe4/0.assembleClusters/myersPopGen_100_085_05.json\n",
      "loading Assembly: myersPopGen_50_085_05\n",
      "from saved path: /gpfs/loomis/scratch60/skelly/nbe4/0.assembleClusters/myersPopGen_50_085_05.json\n",
      "loading Assembly: myersPopGen_25_09_05\n",
      "from saved path: /gpfs/loomis/scratch60/skelly/nbe4/0.assembleClusters/myersPopGen_25_09_05.json\n",
      "loading Assembly: myersPopGen_50_095_05\n",
      "from saved path: /gpfs/loomis/scratch60/skelly/nbe4/0.assembleClusters/myersPopGen_50_095_05.json\n",
      "loading Assembly: myersPopGen_100_09_02\n",
      "from saved path: /gpfs/loomis/scratch60/skelly/nbe4/0.assembleClusters/myersPopGen_100_09_02.json\n",
      "loading Assembly: myersPopGen_100_085_035\n",
      "from saved path: /gpfs/loomis/scratch60/skelly/nbe4/0.assembleClusters/myersPopGen_100_085_035.json\n",
      "loading Assembly: myersPopGen_50_085_035\n",
      "from saved path: /gpfs/loomis/scratch60/skelly/nbe4/0.assembleClusters/myersPopGen_50_085_035.json\n",
      "loading Assembly: myersPopGen_25_09_035\n",
      "from saved path: /gpfs/loomis/scratch60/skelly/nbe4/0.assembleClusters/myersPopGen_25_09_035.json\n",
      "loading Assembly: myersPopGen_25_095_05\n",
      "from saved path: /gpfs/loomis/scratch60/skelly/nbe4/0.assembleClusters/myersPopGen_25_095_05.json\n",
      "loading Assembly: myersPopGen_100_095_035\n",
      "from saved path: /gpfs/loomis/scratch60/skelly/nbe4/0.assembleClusters/myersPopGen_100_095_035.json\n",
      "loading Assembly: myersPopGen_50_095_02\n",
      "from saved path: /gpfs/loomis/scratch60/skelly/nbe4/0.assembleClusters/myersPopGen_50_095_02.json\n",
      "loading Assembly: myersPopGen_25_085_02\n",
      "from saved path: /gpfs/loomis/scratch60/skelly/nbe4/0.assembleClusters/myersPopGen_25_085_02.json\n",
      "loading Assembly: myersPopGen_10000_095_05\n",
      "from saved path: /gpfs/loomis/scratch60/skelly/nbe4/0.assembleClusters/myersPopGen_10000_095_05.json\n",
      "loading Assembly: myersPopGen_50_085_02\n",
      "from saved path: /gpfs/loomis/scratch60/skelly/nbe4/0.assembleClusters/myersPopGen_50_085_02.json\n"
     ]
    }
   ],
   "source": [
    "for f in os.listdir(workDir):\n",
    "    if \"json\" in f:\n",
    "        try:\n",
    "            thisRun=ip.load_json(join(workDir,f))\n",
    "            #utDir=join(workDir,f.split(\".\")[0]+\"_outfiles\")\n",
    "            mainStats=join(outDir,f.split(\".\")[0]+\"_finalStats.txt\")\n",
    "            statsFrame=thisRun.stats\n",
    "            statsFrame.rename(columns={'':'sampleName'})\n",
    "            statsFrame['maxDepth']=f.split(\"_\")[1]\n",
    "            statsFrame['clust_threshold']=f.split(\"_\")[2]\n",
    "            statsFrame['max_shared_Hs_locus']=f.split(\"_\")[3].split(\".\")[0]\n",
    "            pandas.DataFrame.to_csv(statsFrame, mainStats)\n",
    "        except FileNotFoundError:\n",
    "            pass\n",
    "        except IndexError:\n",
    "            pass\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
