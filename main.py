import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
# from matplotlib.animation import PillowWriter, FFMpegWriter       #for saving in GIF
import argparse

import sort

#note that the step counting isn't accurate - some algorithms stop at multiple times in order to make better coloring

#######################################################

def parse_args():
    parser = argparse.ArgumentParser()

    parser.add_argument('-n', type=int, default=100, help='Number of elements in an array.')
    parser.add_argument('-m', type=int, default=0, help='Min element value.')
    parser.add_argument('-M', type=int, default=100, help='Max element value.')

    parser.add_argument('-r', '--random', action='store_true', help='Generate random values (from uniform distribution) instead of values in range.')

    parser.add_argument('--updateTick', type=int, default=1, help='Determines the delay between frame updates.')
    parser.add_argument('--noAnim', action='store_true', help='Skip the animation & show only the sorted array.')

    alg_names = list(sort.algs.keys())
    parser.add_argument('alg', nargs='?', type=str, choices=alg_names, default=alg_names[0], help='What type of sorting algorithm should be used.')

    args = parser.parse_args()

    if not args.random:
        args.m,args.M = 0,args.n

    return args

#######################################################

def main(args):
    print(f"Using {args.alg} sort")
    fig, ax = plt.subplots()
    bars = plt.bar(np.arange(args.n)+0.5, np.zeros(args.n))
    text = plt.text(0, args.M+1, "Step: 0")
    ln, = plt.plot([-5, args.n+5], [-1,-1], c='r')
    drawInSteps = not args.noAnim

    if not args.random:
        data = np.random.permutation(args.n)+1
    else:
        data = np.random.uniform(args.m, args.M, args.n)
    # alg = sortingAlg(data, drawInSteps)
    alg = sort.algs[args.alg](data, drawInSteps)

    def redraw(data, anc):
        #update data values
        for i in range(args.n):
            bars[i].set_height(data[i])
            bars[i].set_color('dodgerblue')
        
        #update value highlights
        for color,idx in anc.items():
            if type(idx) == list:
                for i in idx:
                    if i >= 0:
                        bars[i].set_color(color)
            else:
                if idx >= 0:
                    bars[idx].set_color(color)
        
        ln.set_ydata([alg.horLine, alg.horLine])

    def valueCheck():
        val = np.arange(args.n)+1
        mismatch = False
        for i in range(val.size):
            if val[i] != alg.data[i]:
                print(f"data[{i}] != {i} ({data[i]})")
                mismatch = True
                break
        if not mismatch:
            print("Values match")

    def animInit():
        ax.set_xlim(0, args.n, 1)
        ax.set_ylim(args.m, args.M)
        
        redraw(alg.data, alg.anc)

    def animUpdate(frame):
        alg.update()

        if alg.sorted:
            valueCheck()
        
        redraw(alg.data, alg.anc)
        text.set_text("Comparisons: {}, Array accesses: {}".format(alg.cc, alg.ca))

    ani = FuncAnimation(fig, animUpdate, frames=alg.stepGen(), init_func=animInit, interval=args.updateTick, repeat=False)
    print("Done")
    plt.show()
    # ani.save("anim.gif", dpi=300, writer=PillowWriter(fps=25))
    # plt.close()

if __name__ == "__main__":
    args = parse_args()
    main(args)