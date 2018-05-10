#! /usr/bin/env python

# Install tensorflow and required packages
# Deploy this script on the cloud
# Prepare the checkpoint
# Prepare the vocab

import re
import tensorflow as tf
import numpy as np
import os
# import data_helpers
from tensorflow.contrib import learn
import csv

# input_data_file = './data/four_class/class_two.test' # the command line prompt will ask for input_data_file

def clean_str(string):
    string = re.sub(r"[^A-Za-z0-9(),!?\'\`]", " ", string)
    string = re.sub(r"\'s", " \'s", string)
    string = re.sub(r"\'ve", " \'ve", string)
    string = re.sub(r"n\'t", " n\'t", string)
    string = re.sub(r"\'re", " \'re", string)
    string = re.sub(r"\'d", " \'d", string)
    string = re.sub(r"\'ll", " \'ll", string)
    string = re.sub(r",", " , ", string)
    string = re.sub(r"!", " ! ", string)
    string = re.sub(r"\(", " \( ", string)
    string = re.sub(r"\)", " \) ", string)
    string = re.sub(r"\?", " \? ", string)
    string = re.sub(r"\s{2,}", " ", string)
    return string.strip().lower()

def load_unlabeled_data(input_text_file):
    input_x = list(open(input_text_file, 'r').readlines())
    input_x = [s.strip() for s in input_x]
    input_x = [clean_str(s) for s in input_x]
    return input_x

# Input from the command line

tf.flags.DEFINE_string("checkpoint_dir", "", "Checkpoint directory from training run")
tf.flags.DEFINE_string("input_data_file", "", "path to the input unlabeled text file")

# Optional stuff
tf.flags.DEFINE_integer("batch_size", 64, "Batch Size (default: 64)")
tf.flags.DEFINE_boolean("allow_soft_placement", True, "Allow device soft device placement")
tf.flags.DEFINE_boolean("log_device_placement", False, "Log placement of ops on devices")


def get_predicted_label(text_list):
    FLAGS = tf.flags.FLAGS
    # x_raw = load_unlabeled_data(FLAGS.input_data_file)

    x_raw = text_list

    # Map data into vocabulary
    vocab_path = "./runs/vocab"
    vocab_processor = learn.preprocessing.VocabularyProcessor.restore(vocab_path)
    x_test = np.array(list(vocab_processor.transform(x_raw)))

    # Evaluation
    # ==================================================
    # checkpoint_file = tf.train.latest_checkpoint("./runs/checkpoints/")
    checkpoint_file = './runs/checkpoints/model-13900'
    graph = tf.Graph()
    with graph.as_default():
        session_conf = tf.ConfigProto(
          allow_soft_placement=FLAGS.allow_soft_placement,
          log_device_placement=FLAGS.log_device_placement)
        sess = tf.Session(config=session_conf)
        with sess.as_default():
            # Load the saved meta graph and restore variables
            saver = tf.train.import_meta_graph("{}.meta".format(checkpoint_file))
            saver.restore(sess, checkpoint_file)

            # Get the placeholders from the graph by name
            input_x = graph.get_operation_by_name("input_x").outputs[0]
            # input_y = graph.get_operation_by_name("input_y").outputs[0]
            dropout_keep_prob = graph.get_operation_by_name("dropout_keep_prob").outputs[0]

            # Tensors we want to evaluate
            predictions = graph.get_operation_by_name("output/predictions").outputs[0]

            # Generate batches for one epoch
            # batches = data_helpers.batch_iter(list(x_test), FLAGS.batch_size, 1, shuffle=False)

            # Collect the predictions here
            all_predictions = []

            # for x_test_batch in batches:
            #     batch_predictions = sess.run(predictions, {input_x: x_test_batch, dropout_keep_prob: 1.0})
            #     all_predictions = np.concatenate([all_predictions, batch_predictions])

            all_predictions = sess.run(predictions, {input_x: x_test, dropout_keep_prob: 1.0})

            # for predicted_label in all_predictions:
            #     print(predicted_label)
            native_list = []
            for ele in all_predictions:
                native_list.append(ele.item())
        return native_list




'''
predictions_human_readable = np.column_stack((np.array(x_raw), all_predictions))
out_path = os.path.join(FLAGS.checkpoint_dir, "..", "text_and_predicted_result.csv")
print("Saving evaluation to {0}".format(out_path))

with open(out_path, 'w') as f:
    csv.writer(f).writerows(predictions_human_readable)
'''
