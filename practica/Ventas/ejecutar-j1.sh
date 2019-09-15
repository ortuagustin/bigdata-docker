hdfs dfs -rm -r result || ejecutarHadoopStreamingPython.sh Ventas/data result /home/big_data/practica/Ventas/mapper-j1.py /home/big_data/practica/Ventas/reducer-j1.py

rm -rf result && hdfs dfs -copyToLocal result result