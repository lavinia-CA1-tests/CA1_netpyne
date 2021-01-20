set yrange [0:200]
set xrange [0:200]
set zrange [100:155]
splot 'xyz.dat' u 2:3:4:1 lc variable pt 7 ps 1 t"

