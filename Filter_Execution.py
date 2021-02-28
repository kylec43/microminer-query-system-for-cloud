def Execute_Filters(data, *filters):

	transformed_data = data

	for filter in filters:
		filter.Add_Data(transformed_data)
		transformed_data = filter.Get_Transformed_Data()

	return transformed_data


