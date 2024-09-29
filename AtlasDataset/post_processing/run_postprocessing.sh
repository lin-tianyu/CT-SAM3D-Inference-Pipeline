INPUT_FOLDER="/root/autodl-tmp/AbdomenAtlasDemoPredictSourceDAPformat"
PP_OUTPUT="/root/autodl-tmp/AbdomenAtlasDemoPredictSourceDAPpostprocessed"
NOF_JOBS=4

python post_processing/post_process_volumes.py \
    --source_dir $INPUT_FOLDER \
    --target_dir $PP_OUTPUT \
    --nof_jobs $NOF_JOBS