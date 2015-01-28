add_library(d3t12_rest
	curl_output_init.c
	curl_output_free.c
	curl_output_write_data_overwrite.c

	CURLGetter.cc
	AtlasJSONDecoder.cc
)