import cv2
import tensorflow as tf
import numpy as np

#White Regions Range
hue_l = 0
lit_l = 225
sat_l = 0

hue_l_y = 30
hue_h_y = 33
lit_l_y = 160
sat_l_y = 0


def clr_segment(hls, lower_range, upper_range):
    mask_in_range = cv2.inRange(hls, lower_range, upper_range)
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3,3))
    mask_dilated = cv2.morphologyEx(mask_in_range, cv2.MORPH_DILATE, kernel)
    return mask_dilated


def segment_lanes(frame, min_area):
    hls = cv2.cvtColor(frame, cv2.COLOR_BGR2HLS)

    # Segmenting White regions
    white_regions = clr_segment(hls, np.array([hue_l, lit_l, sat_l]), np.array([255,255,255]))

    yellow_regions = clr_segment(hls, np.array([hue_l_y, lit_l_y, sat_l_y]), np.array([hue_h_y, 255, 255]))

    cv2.imshow("white_regions", white_regions)
    cv2.imshow("yellow_regions", yellow_regions)

    cv2.waitKey(1)


