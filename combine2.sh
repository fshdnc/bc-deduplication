#cd /scratch/project_2002085/lihsin/dedup
#touch cache.txt
cd /scratch/project_2002085/lihsin/XLM/data/bookcorpus-partial-111119_contentfiltered/
pwd
awk 'FNR==1{print "\n\n</doc>\n\n<doc>\n\n"}1' z*.txt > /scratch/project_2002085/lihsin/dedup/finalfile.txt

#for file in 
#    do
#    cat cache.txt doc.txt $file > cache.txt 
#    done
