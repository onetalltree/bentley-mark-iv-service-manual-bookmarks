PYTHON = python3

SRC_DIR = ./src

DATA_DIR = ./definitions
TOC_DIR = $(DATA_DIR)/TableOfContents
INDEX_DIR = $(DATA_DIR)/Index
ADDITIONAL_DIR = $(DATA_DIR)/Additional

BUILD_DIR = ./build
OUT_DIR = .

$(OUT_DIR)/bookmarks.txt: $(BUILD_DIR)/toc_bookmarks.txt $(BUILD_DIR)/additional_bookmarks.txt
	cat $^ > $@

# Table of contents bookmarks

$(BUILD_DIR)/toc_bookmarks.txt: $(TOC_DIR)/bookmarks.json
	@mkdir -p $(BUILD_DIR)
	$(PYTHON) $(SRC_DIR)/toc_generate_bookmarks.py < $? > $@

$(TOC_DIR)/bookmarks.json: $(TOC_DIR)/bookmarks.csv
	$(PYTHON) $(SRC_DIR)/toc_convert_csv_to_json.py < $? > $@

# Additional bookmarks
# NOTE: The additional bookmarks csv & json files use the Table of Contents structure

$(BUILD_DIR)/additional_bookmarks.txt : $(ADDITIONAL_DIR)/bookmarks.json
	@mkdir -p $(BUILD_DIR)
	$(PYTHON) $(SRC_DIR)/toc_generate_bookmarks.py < $? > $@

$(ADDITIONAL_DIR)/bookmarks.json: $(ADDITIONAL_DIR)/bookmarks.csv
	$(PYTHON) $(SRC_DIR)/toc_convert_csv_to_json.py < $? > $@
