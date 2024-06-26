import numpy as np
import pandas as pd
import math
import matplotlib.pyplot as plt
from ipywidgets import interact
from google.colab import output
output.enable_custom_widget_manager()
from mpl_toolkits.mplot3d import Axes3D
import copy
from matplotlib import animation
def data_visual_2D(n_features, feature_explanations, X,y):
    plt.close()
    for i in range(n_features):
      feature = list(feature_explanations.keys())[i]
    plt.figure(figsize=(6, 4))
    plt.bar(X[:, i], y)
    plt.xlabel(feature)
    plt.ylabel("Student Rank")
    plt.title(f"{feature} vs Student Rank")
    plt.show()
def plot_3d_graph(X, y):
    plt.close()
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    study_hours = X[:, 0]
    math_score = X[:, 1]
    attendance_percentage = X[:, 4]
    ax.scatter(study_hours, math_score, attendance_percentage, c=y, cmap='viridis')
    ax.set_xlabel('Study Hours')
    ax.set_ylabel('Math Score')
    ax.set_zlabel('Attendance Percentage')
    ax.set_title('Dataset Visualization')
    plt.show()
def cost_vs_iteration(J_history, num_iters):
    plt.figure(figsize=(8, 6))
    plt.plot(range(num_iters), J_history)
    plt.xlabel("Number of Iterations")
    plt.ylabel("Loss")
    plt.title("Loss Curve")
    plt.show()