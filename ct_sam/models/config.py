import os
from easydict import EasyDict as edict

work_dir = os.path.expandvars("$WORK_DIR")
exp_dir = os.path.join(work_dir, "totalseg_experiment")

cfg = edict()
cfg.task = "single-organ-seg"
cfg.dataset = {}
cfg.dataset.type = "SingleOrganDataset"
# data should be converted to RAI， crop_size in order x, y, z
cfg.dataset.default_value = -1024
# linear or nearest
cfg.dataset.interpolation = "linear"
cfg.dataset.patch_size = [64, 64, 64]  # [Z, Y, X]
cfg.dataset.target_spacing = 1.5

cfg.dataset.trainset_csv = os.path.join(exp_dir, "trainset.csv")
cfg.dataset.validset_csv = os.path.join(exp_dir, "validset.csv")
cfg.dataset.testset_csv = os.path.join(exp_dir, "testset.csv")

cfg.dataset.img_dir = os.path.join(exp_dir, "images")
cfg.dataset.msk_dir = os.path.join(exp_dir, "masks")
cfg.dataset.debug_dir = os.path.join(exp_dir, "debug")
cfg.dataset.is_debugging = False
cfg.dataset.num_samples_per_volume = 8
cfg.dataset.max_num_points = 24  # pos/neg
cfg.dataset.prob_gamma = 0.7

cfg.dataset.normalization_params = {}
cfg.dataset.normalization_params.min_value = -125
cfg.dataset.normalization_params.max_value = 225
cfg.dataset.normalization_params.clip = True

cfg.dataset.aug_params = {}
cfg.dataset.aug_params.on = True
cfg.dataset.aug_params.prob = 0.6
cfg.dataset.aug_params.translation = [-20, 20]  # mm
cfg.dataset.aug_params.scale = [0.9, 1.1]  # ratio
# rotation axis defined in rai frame, set it to [0,0,0] for random axis
cfg.dataset.aug_params.rotation_axis = [0, 0, 0]
cfg.dataset.aug_params.rotation_angle = [-10, 10]  # degree

cfg.training_params = {}
# 0 stands for not to resume, while positive numbers stands for the epoch number to resume
cfg.training_params.resume_epoch = 0
cfg.training_params.batch_size = 6
cfg.training_params.num_iters = 5
cfg.training_params.lr_policy = "warm_up_multi_step"
cfg.training_params.warm_up_epochs = 100
cfg.training_params.lr_milestones = [800]
cfg.training_params.max_epochs = 1000
cfg.training_params.save_epochs = 100
cfg.training_params.valid_epoch_freq = 1
# num_threads is for each gpu, not in total
cfg.training_params.num_threads = 2
cfg.training_params.random_seed = 42
cfg.training_params.lr = 1e-4
cfg.training_params.clip_grad = 5
cfg.training_params.use_amp = False
cfg.training_params.save_dir = os.path.join(exp_dir, "models", "ct_sam")

cfg.network = "restv2_tiny"

cfg.loss = {}
# focal loss, dice loss and mix is also allowed
cfg.loss.loss_name = "mix"
cfg.loss.focal_alpha = 0.8
cfg.loss.focal_gamma = 2
cfg.loss.balance = [0.2, 0.8]
