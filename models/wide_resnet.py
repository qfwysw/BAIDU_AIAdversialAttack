from paddle.fluid.initializer import Constant
from paddle.fluid.param_attr import ParamAttr
import paddle.fluid as fluid
__all__ = ["wide_resnet"]
class widenet():
    def __init__(self):
        self.name = 'wide_resnet'
    def x2paddle_net(self,input):
        #_input_1 = fluid.layers.data(shape=[1, 3, 224, 224], name=#'_input_1', dtype='float32', append_batch_size=False)
        _input_1 = input
        _fc_bias = fluid.layers.create_parameter(shape=[121], name='_fc_bias', attr='_fc_bias', default_initializer=Constant(0.0), dtype='float32')
        _fc_weight = fluid.layers.create_parameter(shape=[121, 2048], name='_fc_weight', attr='_fc_weight', default_initializer=Constant(0.0), dtype='float32')
        _321 = fluid.layers.conv2d(_input_1, num_filters=64, bias_attr=False, dilation=[1, 1], stride=[2, 2], name='_321', filter_size=[7, 7], param_attr='_conv1_weight', padding=[3, 3], groups=1)
        _322 = fluid.layers.batch_norm(_321, name='_322', data_layout='NCHW', epsilon=9.999999747378752e-06, moving_mean_name='_bn1_running_mean', momentum=0.8999999761581421, use_global_stats=False, is_test=True, moving_variance_name='_bn1_running_var', param_attr='_bn1_weight', bias_attr='_bn1_bias')
        _323 = fluid.layers.relu(_322, name='_323')
        _324 = fluid.layers.pool2d(_323, exclusive=False, pool_padding=[1, 1], pool_type='max', name='_324', ceil_mode=False, pool_size=[3, 3], pool_stride=[2, 2])
        _325 = fluid.layers.conv2d(_324, num_filters=128, bias_attr=False, dilation=[1, 1], stride=[1, 1], name='_325', filter_size=[1, 1], param_attr='_layer1_0_conv1_weight', padding=[0, 0], groups=1)
        _333 = fluid.layers.conv2d(_324, num_filters=256, bias_attr=False, dilation=[1, 1], stride=[1, 1], name='_333', filter_size=[1, 1], param_attr='_layer1_0_downsample_0_weight', padding=[0, 0], groups=1)
        _326 = fluid.layers.batch_norm(_325, name='_326', data_layout='NCHW', epsilon=9.999999747378752e-06, moving_mean_name='_layer1_0_bn1_running_mean', momentum=0.8999999761581421, use_global_stats=False, is_test=True, moving_variance_name='_layer1_0_bn1_running_var', param_attr='_layer1_0_bn1_weight', bias_attr='_layer1_0_bn1_bias')
        _334 = fluid.layers.batch_norm(_333, name='_334', data_layout='NCHW', epsilon=9.999999747378752e-06, moving_mean_name='_layer1_0_downsample_1_running_mean', momentum=0.8999999761581421, use_global_stats=False, is_test=True, moving_variance_name='_layer1_0_downsample_1_running_var', param_attr='_layer1_0_downsample_1_weight', bias_attr='_layer1_0_downsample_1_bias')
        _327 = fluid.layers.relu(_326, name='_327')
        _328 = fluid.layers.conv2d(_327, num_filters=128, bias_attr=False, dilation=[1, 1], stride=[1, 1], name='_328', filter_size=[3, 3], param_attr='_layer1_0_conv2_weight', padding=[1, 1], groups=1)
        _329 = fluid.layers.batch_norm(_328, name='_329', data_layout='NCHW', epsilon=9.999999747378752e-06, moving_mean_name='_layer1_0_bn2_running_mean', momentum=0.8999999761581421, use_global_stats=False, is_test=True, moving_variance_name='_layer1_0_bn2_running_var', param_attr='_layer1_0_bn2_weight', bias_attr='_layer1_0_bn2_bias')
        _330 = fluid.layers.relu(_329, name='_330')
        _331 = fluid.layers.conv2d(_330, num_filters=256, bias_attr=False, dilation=[1, 1], stride=[1, 1], name='_331', filter_size=[1, 1], param_attr='_layer1_0_conv3_weight', padding=[0, 0], groups=1)
        _332 = fluid.layers.batch_norm(_331, name='_332', data_layout='NCHW', epsilon=9.999999747378752e-06, moving_mean_name='_layer1_0_bn3_running_mean', momentum=0.8999999761581421, use_global_stats=False, is_test=True, moving_variance_name='_layer1_0_bn3_running_var', param_attr='_layer1_0_bn3_weight', bias_attr='_layer1_0_bn3_bias')
        _335 = fluid.layers.elementwise_add(x=_332, y=_334, name='_335')
        _336 = fluid.layers.relu(_335, name='_336')
        _337 = fluid.layers.conv2d(_336, num_filters=128, bias_attr=False, dilation=[1, 1], stride=[1, 1], name='_337', filter_size=[1, 1], param_attr='_layer1_1_conv1_weight', padding=[0, 0], groups=1)
        _338 = fluid.layers.batch_norm(_337, name='_338', data_layout='NCHW', epsilon=9.999999747378752e-06, moving_mean_name='_layer1_1_bn1_running_mean', momentum=0.8999999761581421, use_global_stats=False, is_test=True, moving_variance_name='_layer1_1_bn1_running_var', param_attr='_layer1_1_bn1_weight', bias_attr='_layer1_1_bn1_bias')
        _339 = fluid.layers.relu(_338, name='_339')
        _340 = fluid.layers.conv2d(_339, num_filters=128, bias_attr=False, dilation=[1, 1], stride=[1, 1], name='_340', filter_size=[3, 3], param_attr='_layer1_1_conv2_weight', padding=[1, 1], groups=1)
        _341 = fluid.layers.batch_norm(_340, name='_341', data_layout='NCHW', epsilon=9.999999747378752e-06, moving_mean_name='_layer1_1_bn2_running_mean', momentum=0.8999999761581421, use_global_stats=False, is_test=True, moving_variance_name='_layer1_1_bn2_running_var', param_attr='_layer1_1_bn2_weight', bias_attr='_layer1_1_bn2_bias')
        _342 = fluid.layers.relu(_341, name='_342')
        _343 = fluid.layers.conv2d(_342, num_filters=256, bias_attr=False, dilation=[1, 1], stride=[1, 1], name='_343', filter_size=[1, 1], param_attr='_layer1_1_conv3_weight', padding=[0, 0], groups=1)
        _344 = fluid.layers.batch_norm(_343, name='_344', data_layout='NCHW', epsilon=9.999999747378752e-06, moving_mean_name='_layer1_1_bn3_running_mean', momentum=0.8999999761581421, use_global_stats=False, is_test=True, moving_variance_name='_layer1_1_bn3_running_var', param_attr='_layer1_1_bn3_weight', bias_attr='_layer1_1_bn3_bias')
        _345 = fluid.layers.elementwise_add(x=_344, y=_336, name='_345')
        _346 = fluid.layers.relu(_345, name='_346')
        _347 = fluid.layers.conv2d(_346, num_filters=128, bias_attr=False, dilation=[1, 1], stride=[1, 1], name='_347', filter_size=[1, 1], param_attr='_layer1_2_conv1_weight', padding=[0, 0], groups=1)
        _348 = fluid.layers.batch_norm(_347, name='_348', data_layout='NCHW', epsilon=9.999999747378752e-06, moving_mean_name='_layer1_2_bn1_running_mean', momentum=0.8999999761581421, use_global_stats=False, is_test=True, moving_variance_name='_layer1_2_bn1_running_var', param_attr='_layer1_2_bn1_weight', bias_attr='_layer1_2_bn1_bias')
        _349 = fluid.layers.relu(_348, name='_349')
        _350 = fluid.layers.conv2d(_349, num_filters=128, bias_attr=False, dilation=[1, 1], stride=[1, 1], name='_350', filter_size=[3, 3], param_attr='_layer1_2_conv2_weight', padding=[1, 1], groups=1)
        _351 = fluid.layers.batch_norm(_350, name='_351', data_layout='NCHW', epsilon=9.999999747378752e-06, moving_mean_name='_layer1_2_bn2_running_mean', momentum=0.8999999761581421, use_global_stats=False, is_test=True, moving_variance_name='_layer1_2_bn2_running_var', param_attr='_layer1_2_bn2_weight', bias_attr='_layer1_2_bn2_bias')
        _352 = fluid.layers.relu(_351, name='_352')
        _353 = fluid.layers.conv2d(_352, num_filters=256, bias_attr=False, dilation=[1, 1], stride=[1, 1], name='_353', filter_size=[1, 1], param_attr='_layer1_2_conv3_weight', padding=[0, 0], groups=1)
        _354 = fluid.layers.batch_norm(_353, name='_354', data_layout='NCHW', epsilon=9.999999747378752e-06, moving_mean_name='_layer1_2_bn3_running_mean', momentum=0.8999999761581421, use_global_stats=False, is_test=True, moving_variance_name='_layer1_2_bn3_running_var', param_attr='_layer1_2_bn3_weight', bias_attr='_layer1_2_bn3_bias')
        _355 = fluid.layers.elementwise_add(x=_354, y=_346, name='_355')
        _356 = fluid.layers.relu(_355, name='_356')
        _357 = fluid.layers.conv2d(_356, num_filters=256, bias_attr=False, dilation=[1, 1], stride=[1, 1], name='_357', filter_size=[1, 1], param_attr='_layer2_0_conv1_weight', padding=[0, 0], groups=1)
        _365 = fluid.layers.conv2d(_356, num_filters=512, bias_attr=False, dilation=[1, 1], stride=[2, 2], name='_365', filter_size=[1, 1], param_attr='_layer2_0_downsample_0_weight', padding=[0, 0], groups=1)
        _358 = fluid.layers.batch_norm(_357, name='_358', data_layout='NCHW', epsilon=9.999999747378752e-06, moving_mean_name='_layer2_0_bn1_running_mean', momentum=0.8999999761581421, use_global_stats=False, is_test=True, moving_variance_name='_layer2_0_bn1_running_var', param_attr='_layer2_0_bn1_weight', bias_attr='_layer2_0_bn1_bias')
        _366 = fluid.layers.batch_norm(_365, name='_366', data_layout='NCHW', epsilon=9.999999747378752e-06, moving_mean_name='_layer2_0_downsample_1_running_mean', momentum=0.8999999761581421, use_global_stats=False, is_test=True, moving_variance_name='_layer2_0_downsample_1_running_var', param_attr='_layer2_0_downsample_1_weight', bias_attr='_layer2_0_downsample_1_bias')
        _359 = fluid.layers.relu(_358, name='_359')
        _360 = fluid.layers.conv2d(_359, num_filters=256, bias_attr=False, dilation=[1, 1], stride=[2, 2], name='_360', filter_size=[3, 3], param_attr='_layer2_0_conv2_weight', padding=[1, 1], groups=1)
        _361 = fluid.layers.batch_norm(_360, name='_361', data_layout='NCHW', epsilon=9.999999747378752e-06, moving_mean_name='_layer2_0_bn2_running_mean', momentum=0.8999999761581421, use_global_stats=False, is_test=True, moving_variance_name='_layer2_0_bn2_running_var', param_attr='_layer2_0_bn2_weight', bias_attr='_layer2_0_bn2_bias')
        _362 = fluid.layers.relu(_361, name='_362')
        _363 = fluid.layers.conv2d(_362, num_filters=512, bias_attr=False, dilation=[1, 1], stride=[1, 1], name='_363', filter_size=[1, 1], param_attr='_layer2_0_conv3_weight', padding=[0, 0], groups=1)
        _364 = fluid.layers.batch_norm(_363, name='_364', data_layout='NCHW', epsilon=9.999999747378752e-06, moving_mean_name='_layer2_0_bn3_running_mean', momentum=0.8999999761581421, use_global_stats=False, is_test=True, moving_variance_name='_layer2_0_bn3_running_var', param_attr='_layer2_0_bn3_weight', bias_attr='_layer2_0_bn3_bias')
        _367 = fluid.layers.elementwise_add(x=_364, y=_366, name='_367')
        _368 = fluid.layers.relu(_367, name='_368')
        _369 = fluid.layers.conv2d(_368, num_filters=256, bias_attr=False, dilation=[1, 1], stride=[1, 1], name='_369', filter_size=[1, 1], param_attr='_layer2_1_conv1_weight', padding=[0, 0], groups=1)
        _370 = fluid.layers.batch_norm(_369, name='_370', data_layout='NCHW', epsilon=9.999999747378752e-06, moving_mean_name='_layer2_1_bn1_running_mean', momentum=0.8999999761581421, use_global_stats=False, is_test=True, moving_variance_name='_layer2_1_bn1_running_var', param_attr='_layer2_1_bn1_weight', bias_attr='_layer2_1_bn1_bias')
        _371 = fluid.layers.relu(_370, name='_371')
        _372 = fluid.layers.conv2d(_371, num_filters=256, bias_attr=False, dilation=[1, 1], stride=[1, 1], name='_372', filter_size=[3, 3], param_attr='_layer2_1_conv2_weight', padding=[1, 1], groups=1)
        _373 = fluid.layers.batch_norm(_372, name='_373', data_layout='NCHW', epsilon=9.999999747378752e-06, moving_mean_name='_layer2_1_bn2_running_mean', momentum=0.8999999761581421, use_global_stats=False, is_test=True, moving_variance_name='_layer2_1_bn2_running_var', param_attr='_layer2_1_bn2_weight', bias_attr='_layer2_1_bn2_bias')
        _374 = fluid.layers.relu(_373, name='_374')
        _375 = fluid.layers.conv2d(_374, num_filters=512, bias_attr=False, dilation=[1, 1], stride=[1, 1], name='_375', filter_size=[1, 1], param_attr='_layer2_1_conv3_weight', padding=[0, 0], groups=1)
        _376 = fluid.layers.batch_norm(_375, name='_376', data_layout='NCHW', epsilon=9.999999747378752e-06, moving_mean_name='_layer2_1_bn3_running_mean', momentum=0.8999999761581421, use_global_stats=False, is_test=True, moving_variance_name='_layer2_1_bn3_running_var', param_attr='_layer2_1_bn3_weight', bias_attr='_layer2_1_bn3_bias')
        _377 = fluid.layers.elementwise_add(x=_376, y=_368, name='_377')
        _378 = fluid.layers.relu(_377, name='_378')
        _379 = fluid.layers.conv2d(_378, num_filters=256, bias_attr=False, dilation=[1, 1], stride=[1, 1], name='_379', filter_size=[1, 1], param_attr='_layer2_2_conv1_weight', padding=[0, 0], groups=1)
        _380 = fluid.layers.batch_norm(_379, name='_380', data_layout='NCHW', epsilon=9.999999747378752e-06, moving_mean_name='_layer2_2_bn1_running_mean', momentum=0.8999999761581421, use_global_stats=False, is_test=True, moving_variance_name='_layer2_2_bn1_running_var', param_attr='_layer2_2_bn1_weight', bias_attr='_layer2_2_bn1_bias')
        _381 = fluid.layers.relu(_380, name='_381')
        _382 = fluid.layers.conv2d(_381, num_filters=256, bias_attr=False, dilation=[1, 1], stride=[1, 1], name='_382', filter_size=[3, 3], param_attr='_layer2_2_conv2_weight', padding=[1, 1], groups=1)
        _383 = fluid.layers.batch_norm(_382, name='_383', data_layout='NCHW', epsilon=9.999999747378752e-06, moving_mean_name='_layer2_2_bn2_running_mean', momentum=0.8999999761581421, use_global_stats=False, is_test=True, moving_variance_name='_layer2_2_bn2_running_var', param_attr='_layer2_2_bn2_weight', bias_attr='_layer2_2_bn2_bias')
        _384 = fluid.layers.relu(_383, name='_384')
        _385 = fluid.layers.conv2d(_384, num_filters=512, bias_attr=False, dilation=[1, 1], stride=[1, 1], name='_385', filter_size=[1, 1], param_attr='_layer2_2_conv3_weight', padding=[0, 0], groups=1)
        _386 = fluid.layers.batch_norm(_385, name='_386', data_layout='NCHW', epsilon=9.999999747378752e-06, moving_mean_name='_layer2_2_bn3_running_mean', momentum=0.8999999761581421, use_global_stats=False, is_test=True, moving_variance_name='_layer2_2_bn3_running_var', param_attr='_layer2_2_bn3_weight', bias_attr='_layer2_2_bn3_bias')
        _387 = fluid.layers.elementwise_add(x=_386, y=_378, name='_387')
        _388 = fluid.layers.relu(_387, name='_388')
        _389 = fluid.layers.conv2d(_388, num_filters=256, bias_attr=False, dilation=[1, 1], stride=[1, 1], name='_389', filter_size=[1, 1], param_attr='_layer2_3_conv1_weight', padding=[0, 0], groups=1)
        _390 = fluid.layers.batch_norm(_389, name='_390', data_layout='NCHW', epsilon=9.999999747378752e-06, moving_mean_name='_layer2_3_bn1_running_mean', momentum=0.8999999761581421, use_global_stats=False, is_test=True, moving_variance_name='_layer2_3_bn1_running_var', param_attr='_layer2_3_bn1_weight', bias_attr='_layer2_3_bn1_bias')
        _391 = fluid.layers.relu(_390, name='_391')
        _392 = fluid.layers.conv2d(_391, num_filters=256, bias_attr=False, dilation=[1, 1], stride=[1, 1], name='_392', filter_size=[3, 3], param_attr='_layer2_3_conv2_weight', padding=[1, 1], groups=1)
        _393 = fluid.layers.batch_norm(_392, name='_393', data_layout='NCHW', epsilon=9.999999747378752e-06, moving_mean_name='_layer2_3_bn2_running_mean', momentum=0.8999999761581421, use_global_stats=False, is_test=True, moving_variance_name='_layer2_3_bn2_running_var', param_attr='_layer2_3_bn2_weight', bias_attr='_layer2_3_bn2_bias')
        _394 = fluid.layers.relu(_393, name='_394')
        _395 = fluid.layers.conv2d(_394, num_filters=512, bias_attr=False, dilation=[1, 1], stride=[1, 1], name='_395', filter_size=[1, 1], param_attr='_layer2_3_conv3_weight', padding=[0, 0], groups=1)
        _396 = fluid.layers.batch_norm(_395, name='_396', data_layout='NCHW', epsilon=9.999999747378752e-06, moving_mean_name='_layer2_3_bn3_running_mean', momentum=0.8999999761581421, use_global_stats=False, is_test=True, moving_variance_name='_layer2_3_bn3_running_var', param_attr='_layer2_3_bn3_weight', bias_attr='_layer2_3_bn3_bias')
        _397 = fluid.layers.elementwise_add(x=_396, y=_388, name='_397')
        _398 = fluid.layers.relu(_397, name='_398')
        _399 = fluid.layers.conv2d(_398, num_filters=512, bias_attr=False, dilation=[1, 1], stride=[1, 1], name='_399', filter_size=[1, 1], param_attr='_layer3_0_conv1_weight', padding=[0, 0], groups=1)
        _407 = fluid.layers.conv2d(_398, num_filters=1024, bias_attr=False, dilation=[1, 1], stride=[2, 2], name='_407', filter_size=[1, 1], param_attr='_layer3_0_downsample_0_weight', padding=[0, 0], groups=1)
        _400 = fluid.layers.batch_norm(_399, name='_400', data_layout='NCHW', epsilon=9.999999747378752e-06, moving_mean_name='_layer3_0_bn1_running_mean', momentum=0.8999999761581421, use_global_stats=False, is_test=True, moving_variance_name='_layer3_0_bn1_running_var', param_attr='_layer3_0_bn1_weight', bias_attr='_layer3_0_bn1_bias')
        _408 = fluid.layers.batch_norm(_407, name='_408', data_layout='NCHW', epsilon=9.999999747378752e-06, moving_mean_name='_layer3_0_downsample_1_running_mean', momentum=0.8999999761581421, use_global_stats=False, is_test=True, moving_variance_name='_layer3_0_downsample_1_running_var', param_attr='_layer3_0_downsample_1_weight', bias_attr='_layer3_0_downsample_1_bias')
        _401 = fluid.layers.relu(_400, name='_401')
        _402 = fluid.layers.conv2d(_401, num_filters=512, bias_attr=False, dilation=[1, 1], stride=[2, 2], name='_402', filter_size=[3, 3], param_attr='_layer3_0_conv2_weight', padding=[1, 1], groups=1)
        _403 = fluid.layers.batch_norm(_402, name='_403', data_layout='NCHW', epsilon=9.999999747378752e-06, moving_mean_name='_layer3_0_bn2_running_mean', momentum=0.8999999761581421, use_global_stats=False, is_test=True, moving_variance_name='_layer3_0_bn2_running_var', param_attr='_layer3_0_bn2_weight', bias_attr='_layer3_0_bn2_bias')
        _404 = fluid.layers.relu(_403, name='_404')
        _405 = fluid.layers.conv2d(_404, num_filters=1024, bias_attr=False, dilation=[1, 1], stride=[1, 1], name='_405', filter_size=[1, 1], param_attr='_layer3_0_conv3_weight', padding=[0, 0], groups=1)
        _406 = fluid.layers.batch_norm(_405, name='_406', data_layout='NCHW', epsilon=9.999999747378752e-06, moving_mean_name='_layer3_0_bn3_running_mean', momentum=0.8999999761581421, use_global_stats=False, is_test=True, moving_variance_name='_layer3_0_bn3_running_var', param_attr='_layer3_0_bn3_weight', bias_attr='_layer3_0_bn3_bias')
        _409 = fluid.layers.elementwise_add(x=_406, y=_408, name='_409')
        _410 = fluid.layers.relu(_409, name='_410')
        _411 = fluid.layers.conv2d(_410, num_filters=512, bias_attr=False, dilation=[1, 1], stride=[1, 1], name='_411', filter_size=[1, 1], param_attr='_layer3_1_conv1_weight', padding=[0, 0], groups=1)
        _412 = fluid.layers.batch_norm(_411, name='_412', data_layout='NCHW', epsilon=9.999999747378752e-06, moving_mean_name='_layer3_1_bn1_running_mean', momentum=0.8999999761581421, use_global_stats=False, is_test=True, moving_variance_name='_layer3_1_bn1_running_var', param_attr='_layer3_1_bn1_weight', bias_attr='_layer3_1_bn1_bias')
        _413 = fluid.layers.relu(_412, name='_413')
        _414 = fluid.layers.conv2d(_413, num_filters=512, bias_attr=False, dilation=[1, 1], stride=[1, 1], name='_414', filter_size=[3, 3], param_attr='_layer3_1_conv2_weight', padding=[1, 1], groups=1)
        _415 = fluid.layers.batch_norm(_414, name='_415', data_layout='NCHW', epsilon=9.999999747378752e-06, moving_mean_name='_layer3_1_bn2_running_mean', momentum=0.8999999761581421, use_global_stats=False, is_test=True, moving_variance_name='_layer3_1_bn2_running_var', param_attr='_layer3_1_bn2_weight', bias_attr='_layer3_1_bn2_bias')
        _416 = fluid.layers.relu(_415, name='_416')
        _417 = fluid.layers.conv2d(_416, num_filters=1024, bias_attr=False, dilation=[1, 1], stride=[1, 1], name='_417', filter_size=[1, 1], param_attr='_layer3_1_conv3_weight', padding=[0, 0], groups=1)
        _418 = fluid.layers.batch_norm(_417, name='_418', data_layout='NCHW', epsilon=9.999999747378752e-06, moving_mean_name='_layer3_1_bn3_running_mean', momentum=0.8999999761581421, use_global_stats=False, is_test=True, moving_variance_name='_layer3_1_bn3_running_var', param_attr='_layer3_1_bn3_weight', bias_attr='_layer3_1_bn3_bias')
        _419 = fluid.layers.elementwise_add(x=_418, y=_410, name='_419')
        _420 = fluid.layers.relu(_419, name='_420')
        _421 = fluid.layers.conv2d(_420, num_filters=512, bias_attr=False, dilation=[1, 1], stride=[1, 1], name='_421', filter_size=[1, 1], param_attr='_layer3_2_conv1_weight', padding=[0, 0], groups=1)
        _422 = fluid.layers.batch_norm(_421, name='_422', data_layout='NCHW', epsilon=9.999999747378752e-06, moving_mean_name='_layer3_2_bn1_running_mean', momentum=0.8999999761581421, use_global_stats=False, is_test=True, moving_variance_name='_layer3_2_bn1_running_var', param_attr='_layer3_2_bn1_weight', bias_attr='_layer3_2_bn1_bias')
        _423 = fluid.layers.relu(_422, name='_423')
        _424 = fluid.layers.conv2d(_423, num_filters=512, bias_attr=False, dilation=[1, 1], stride=[1, 1], name='_424', filter_size=[3, 3], param_attr='_layer3_2_conv2_weight', padding=[1, 1], groups=1)
        _425 = fluid.layers.batch_norm(_424, name='_425', data_layout='NCHW', epsilon=9.999999747378752e-06, moving_mean_name='_layer3_2_bn2_running_mean', momentum=0.8999999761581421, use_global_stats=False, is_test=True, moving_variance_name='_layer3_2_bn2_running_var', param_attr='_layer3_2_bn2_weight', bias_attr='_layer3_2_bn2_bias')
        _426 = fluid.layers.relu(_425, name='_426')
        _427 = fluid.layers.conv2d(_426, num_filters=1024, bias_attr=False, dilation=[1, 1], stride=[1, 1], name='_427', filter_size=[1, 1], param_attr='_layer3_2_conv3_weight', padding=[0, 0], groups=1)
        _428 = fluid.layers.batch_norm(_427, name='_428', data_layout='NCHW', epsilon=9.999999747378752e-06, moving_mean_name='_layer3_2_bn3_running_mean', momentum=0.8999999761581421, use_global_stats=False, is_test=True, moving_variance_name='_layer3_2_bn3_running_var', param_attr='_layer3_2_bn3_weight', bias_attr='_layer3_2_bn3_bias')
        _429 = fluid.layers.elementwise_add(x=_428, y=_420, name='_429')
        _430 = fluid.layers.relu(_429, name='_430')
        _431 = fluid.layers.conv2d(_430, num_filters=512, bias_attr=False, dilation=[1, 1], stride=[1, 1], name='_431', filter_size=[1, 1], param_attr='_layer3_3_conv1_weight', padding=[0, 0], groups=1)
        _432 = fluid.layers.batch_norm(_431, name='_432', data_layout='NCHW', epsilon=9.999999747378752e-06, moving_mean_name='_layer3_3_bn1_running_mean', momentum=0.8999999761581421, use_global_stats=False, is_test=True, moving_variance_name='_layer3_3_bn1_running_var', param_attr='_layer3_3_bn1_weight', bias_attr='_layer3_3_bn1_bias')
        _433 = fluid.layers.relu(_432, name='_433')
        _434 = fluid.layers.conv2d(_433, num_filters=512, bias_attr=False, dilation=[1, 1], stride=[1, 1], name='_434', filter_size=[3, 3], param_attr='_layer3_3_conv2_weight', padding=[1, 1], groups=1)
        _435 = fluid.layers.batch_norm(_434, name='_435', data_layout='NCHW', epsilon=9.999999747378752e-06, moving_mean_name='_layer3_3_bn2_running_mean', momentum=0.8999999761581421, use_global_stats=False, is_test=True, moving_variance_name='_layer3_3_bn2_running_var', param_attr='_layer3_3_bn2_weight', bias_attr='_layer3_3_bn2_bias')
        _436 = fluid.layers.relu(_435, name='_436')
        _437 = fluid.layers.conv2d(_436, num_filters=1024, bias_attr=False, dilation=[1, 1], stride=[1, 1], name='_437', filter_size=[1, 1], param_attr='_layer3_3_conv3_weight', padding=[0, 0], groups=1)
        _438 = fluid.layers.batch_norm(_437, name='_438', data_layout='NCHW', epsilon=9.999999747378752e-06, moving_mean_name='_layer3_3_bn3_running_mean', momentum=0.8999999761581421, use_global_stats=False, is_test=True, moving_variance_name='_layer3_3_bn3_running_var', param_attr='_layer3_3_bn3_weight', bias_attr='_layer3_3_bn3_bias')
        _439 = fluid.layers.elementwise_add(x=_438, y=_430, name='_439')
        _440 = fluid.layers.relu(_439, name='_440')
        _441 = fluid.layers.conv2d(_440, num_filters=512, bias_attr=False, dilation=[1, 1], stride=[1, 1], name='_441', filter_size=[1, 1], param_attr='_layer3_4_conv1_weight', padding=[0, 0], groups=1)
        _442 = fluid.layers.batch_norm(_441, name='_442', data_layout='NCHW', epsilon=9.999999747378752e-06, moving_mean_name='_layer3_4_bn1_running_mean', momentum=0.8999999761581421, use_global_stats=False, is_test=True, moving_variance_name='_layer3_4_bn1_running_var', param_attr='_layer3_4_bn1_weight', bias_attr='_layer3_4_bn1_bias')
        _443 = fluid.layers.relu(_442, name='_443')
        _444 = fluid.layers.conv2d(_443, num_filters=512, bias_attr=False, dilation=[1, 1], stride=[1, 1], name='_444', filter_size=[3, 3], param_attr='_layer3_4_conv2_weight', padding=[1, 1], groups=1)
        _445 = fluid.layers.batch_norm(_444, name='_445', data_layout='NCHW', epsilon=9.999999747378752e-06, moving_mean_name='_layer3_4_bn2_running_mean', momentum=0.8999999761581421, use_global_stats=False, is_test=True, moving_variance_name='_layer3_4_bn2_running_var', param_attr='_layer3_4_bn2_weight', bias_attr='_layer3_4_bn2_bias')
        _446 = fluid.layers.relu(_445, name='_446')
        _447 = fluid.layers.conv2d(_446, num_filters=1024, bias_attr=False, dilation=[1, 1], stride=[1, 1], name='_447', filter_size=[1, 1], param_attr='_layer3_4_conv3_weight', padding=[0, 0], groups=1)
        _448 = fluid.layers.batch_norm(_447, name='_448', data_layout='NCHW', epsilon=9.999999747378752e-06, moving_mean_name='_layer3_4_bn3_running_mean', momentum=0.8999999761581421, use_global_stats=False, is_test=True, moving_variance_name='_layer3_4_bn3_running_var', param_attr='_layer3_4_bn3_weight', bias_attr='_layer3_4_bn3_bias')
        _449 = fluid.layers.elementwise_add(x=_448, y=_440, name='_449')
        _450 = fluid.layers.relu(_449, name='_450')
        _451 = fluid.layers.conv2d(_450, num_filters=512, bias_attr=False, dilation=[1, 1], stride=[1, 1], name='_451', filter_size=[1, 1], param_attr='_layer3_5_conv1_weight', padding=[0, 0], groups=1)
        _452 = fluid.layers.batch_norm(_451, name='_452', data_layout='NCHW', epsilon=9.999999747378752e-06, moving_mean_name='_layer3_5_bn1_running_mean', momentum=0.8999999761581421, use_global_stats=False, is_test=True, moving_variance_name='_layer3_5_bn1_running_var', param_attr='_layer3_5_bn1_weight', bias_attr='_layer3_5_bn1_bias')
        _453 = fluid.layers.relu(_452, name='_453')
        _454 = fluid.layers.conv2d(_453, num_filters=512, bias_attr=False, dilation=[1, 1], stride=[1, 1], name='_454', filter_size=[3, 3], param_attr='_layer3_5_conv2_weight', padding=[1, 1], groups=1)
        _455 = fluid.layers.batch_norm(_454, name='_455', data_layout='NCHW', epsilon=9.999999747378752e-06, moving_mean_name='_layer3_5_bn2_running_mean', momentum=0.8999999761581421, use_global_stats=False, is_test=True, moving_variance_name='_layer3_5_bn2_running_var', param_attr='_layer3_5_bn2_weight', bias_attr='_layer3_5_bn2_bias')
        _456 = fluid.layers.relu(_455, name='_456')
        _457 = fluid.layers.conv2d(_456, num_filters=1024, bias_attr=False, dilation=[1, 1], stride=[1, 1], name='_457', filter_size=[1, 1], param_attr='_layer3_5_conv3_weight', padding=[0, 0], groups=1)
        _458 = fluid.layers.batch_norm(_457, name='_458', data_layout='NCHW', epsilon=9.999999747378752e-06, moving_mean_name='_layer3_5_bn3_running_mean', momentum=0.8999999761581421, use_global_stats=False, is_test=True, moving_variance_name='_layer3_5_bn3_running_var', param_attr='_layer3_5_bn3_weight', bias_attr='_layer3_5_bn3_bias')
        _459 = fluid.layers.elementwise_add(x=_458, y=_450, name='_459')
        _460 = fluid.layers.relu(_459, name='_460')
        _461 = fluid.layers.conv2d(_460, num_filters=1024, bias_attr=False, dilation=[1, 1], stride=[1, 1], name='_461', filter_size=[1, 1], param_attr='_layer4_0_conv1_weight', padding=[0, 0], groups=1)
        _469 = fluid.layers.conv2d(_460, num_filters=2048, bias_attr=False, dilation=[1, 1], stride=[2, 2], name='_469', filter_size=[1, 1], param_attr='_layer4_0_downsample_0_weight', padding=[0, 0], groups=1)
        _462 = fluid.layers.batch_norm(_461, name='_462', data_layout='NCHW', epsilon=9.999999747378752e-06, moving_mean_name='_layer4_0_bn1_running_mean', momentum=0.8999999761581421, use_global_stats=False, is_test=True, moving_variance_name='_layer4_0_bn1_running_var', param_attr='_layer4_0_bn1_weight', bias_attr='_layer4_0_bn1_bias')
        _470 = fluid.layers.batch_norm(_469, name='_470', data_layout='NCHW', epsilon=9.999999747378752e-06, moving_mean_name='_layer4_0_downsample_1_running_mean', momentum=0.8999999761581421, use_global_stats=False, is_test=True, moving_variance_name='_layer4_0_downsample_1_running_var', param_attr='_layer4_0_downsample_1_weight', bias_attr='_layer4_0_downsample_1_bias')
        _463 = fluid.layers.relu(_462, name='_463')
        _464 = fluid.layers.conv2d(_463, num_filters=1024, bias_attr=False, dilation=[1, 1], stride=[2, 2], name='_464', filter_size=[3, 3], param_attr='_layer4_0_conv2_weight', padding=[1, 1], groups=1)
        _465 = fluid.layers.batch_norm(_464, name='_465', data_layout='NCHW', epsilon=9.999999747378752e-06, moving_mean_name='_layer4_0_bn2_running_mean', momentum=0.8999999761581421, use_global_stats=False, is_test=True, moving_variance_name='_layer4_0_bn2_running_var', param_attr='_layer4_0_bn2_weight', bias_attr='_layer4_0_bn2_bias')
        _466 = fluid.layers.relu(_465, name='_466')
        _467 = fluid.layers.conv2d(_466, num_filters=2048, bias_attr=False, dilation=[1, 1], stride=[1, 1], name='_467', filter_size=[1, 1], param_attr='_layer4_0_conv3_weight', padding=[0, 0], groups=1)
        _468 = fluid.layers.batch_norm(_467, name='_468', data_layout='NCHW', epsilon=9.999999747378752e-06, moving_mean_name='_layer4_0_bn3_running_mean', momentum=0.8999999761581421, use_global_stats=False, is_test=True, moving_variance_name='_layer4_0_bn3_running_var', param_attr='_layer4_0_bn3_weight', bias_attr='_layer4_0_bn3_bias')
        _471 = fluid.layers.elementwise_add(x=_468, y=_470, name='_471')
        _472 = fluid.layers.relu(_471, name='_472')
        _473 = fluid.layers.conv2d(_472, num_filters=1024, bias_attr=False, dilation=[1, 1], stride=[1, 1], name='_473', filter_size=[1, 1], param_attr='_layer4_1_conv1_weight', padding=[0, 0], groups=1)
        _474 = fluid.layers.batch_norm(_473, name='_474', data_layout='NCHW', epsilon=9.999999747378752e-06, moving_mean_name='_layer4_1_bn1_running_mean', momentum=0.8999999761581421, use_global_stats=False, is_test=True, moving_variance_name='_layer4_1_bn1_running_var', param_attr='_layer4_1_bn1_weight', bias_attr='_layer4_1_bn1_bias')
        _475 = fluid.layers.relu(_474, name='_475')
        _476 = fluid.layers.conv2d(_475, num_filters=1024, bias_attr=False, dilation=[1, 1], stride=[1, 1], name='_476', filter_size=[3, 3], param_attr='_layer4_1_conv2_weight', padding=[1, 1], groups=1)
        _477 = fluid.layers.batch_norm(_476, name='_477', data_layout='NCHW', epsilon=9.999999747378752e-06, moving_mean_name='_layer4_1_bn2_running_mean', momentum=0.8999999761581421, use_global_stats=False, is_test=True, moving_variance_name='_layer4_1_bn2_running_var', param_attr='_layer4_1_bn2_weight', bias_attr='_layer4_1_bn2_bias')
        _478 = fluid.layers.relu(_477, name='_478')
        _479 = fluid.layers.conv2d(_478, num_filters=2048, bias_attr=False, dilation=[1, 1], stride=[1, 1], name='_479', filter_size=[1, 1], param_attr='_layer4_1_conv3_weight', padding=[0, 0], groups=1)
        _480 = fluid.layers.batch_norm(_479, name='_480', data_layout='NCHW', epsilon=9.999999747378752e-06, moving_mean_name='_layer4_1_bn3_running_mean', momentum=0.8999999761581421, use_global_stats=False, is_test=True, moving_variance_name='_layer4_1_bn3_running_var', param_attr='_layer4_1_bn3_weight', bias_attr='_layer4_1_bn3_bias')
        _481 = fluid.layers.elementwise_add(x=_480, y=_472, name='_481')
        _482 = fluid.layers.relu(_481, name='_482')
        _483 = fluid.layers.conv2d(_482, num_filters=1024, bias_attr=False, dilation=[1, 1], stride=[1, 1], name='_483', filter_size=[1, 1], param_attr='_layer4_2_conv1_weight', padding=[0, 0], groups=1)
        _484 = fluid.layers.batch_norm(_483, name='_484', data_layout='NCHW', epsilon=9.999999747378752e-06, moving_mean_name='_layer4_2_bn1_running_mean', momentum=0.8999999761581421, use_global_stats=False, is_test=True, moving_variance_name='_layer4_2_bn1_running_var', param_attr='_layer4_2_bn1_weight', bias_attr='_layer4_2_bn1_bias')
        _485 = fluid.layers.relu(_484, name='_485')
        _486 = fluid.layers.conv2d(_485, num_filters=1024, bias_attr=False, dilation=[1, 1], stride=[1, 1], name='_486', filter_size=[3, 3], param_attr='_layer4_2_conv2_weight', padding=[1, 1], groups=1)
        _487 = fluid.layers.batch_norm(_486, name='_487', data_layout='NCHW', epsilon=9.999999747378752e-06, moving_mean_name='_layer4_2_bn2_running_mean', momentum=0.8999999761581421, use_global_stats=False, is_test=True, moving_variance_name='_layer4_2_bn2_running_var', param_attr='_layer4_2_bn2_weight', bias_attr='_layer4_2_bn2_bias')
        _488 = fluid.layers.relu(_487, name='_488')
        _489 = fluid.layers.conv2d(_488, num_filters=2048, bias_attr=False, dilation=[1, 1], stride=[1, 1], name='_489', filter_size=[1, 1], param_attr='_layer4_2_conv3_weight', padding=[0, 0], groups=1)
        _490 = fluid.layers.batch_norm(_489, name='_490', data_layout='NCHW', epsilon=9.999999747378752e-06, moving_mean_name='_layer4_2_bn3_running_mean', momentum=0.8999999761581421, use_global_stats=False, is_test=True, moving_variance_name='_layer4_2_bn3_running_var', param_attr='_layer4_2_bn3_weight', bias_attr='_layer4_2_bn3_bias')
        _491 = fluid.layers.elementwise_add(x=_490, y=_482, name='_491')
        _492 = fluid.layers.relu(_491, name='_492')
        _493 = fluid.layers.pool2d(_492, name='_493', pool_type='avg', global_pooling=True)
        _494 = fluid.layers.flatten(_493, name='_494', axis=1)
        _495_mm = fluid.layers.matmul(x=_494, y=_fc_weight, name='_495_mm', transpose_x=False, transpose_y=True, alpha=1.0)
        _495 = fluid.layers.elementwise_add(x=_495_mm, y=_fc_bias, name='_495')
        
        return [_input_1], [_495]


def wide_resnet():
    model = widenet()
    return model