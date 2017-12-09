def combine_boxes(x_arr, y_arr, w_arr, h_arr):
	width_bound = x_arr[0] + w_arr[0]
	height_bound = y_arr[0] + h_arr[0]

	for z in range(1,len(x_arr)):
		diff = (x_arr[z] + w_arr[z]) - width_bound
		if diff > 0:
			w_arr[0] += diff

		diff = (y_arr[z] + h_arr[z]) - height_bound
		if diff > 0:
			h_arr[0] += diff

	return x_arr[0], y_arr[0], w_arr[0], h_arr[0]