start=`date +%s`

for file in ~/packages/sh/install/*
do
  sh $file
done

end=`date +%s`

runtime=$((end-start))
