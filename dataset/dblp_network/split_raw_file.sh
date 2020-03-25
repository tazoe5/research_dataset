if [ $# -ne 1 ]; then
    echo "分割サイズを指定してください"
    exit 1
fi

split_size=$1
dir="./processing_data/size$split_size/"
row_file="./raw_data/dblp_papers_v11.txt"

if [ -d $dir ]; then
    echo "size$split_size found."
else
    echo "make size$split_size"
    mkdir $dir
fi

# num_papers=`cat $row_file | wc -l`
num_papers=4107340 # 先に数えた
num_files=$((num_papers/split_size))
split -l $split_size -a "${#num_files}" $row_file "$dir/file-"
# split -l $split_size -a "${#num_files}" $row_file -d --additional-suffix=.json "$dir/file-"

for file in $(ls $dir); do
    mv "$dir$file" "$dir$file.json"
done
