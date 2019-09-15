hdfs dfs -rm -r result_j2 || ejecutarHadoopStreamingPython.sh file:///home/big_data/practica/result/part-00000 result_j2 /home/big_data/practica/Ventas/mapper-j2.py /home/big_data/practica/Ventas/reducer-j2.py

rm -rf result_j2 && hdfs dfs -copyToLocal result_j2 result_j2