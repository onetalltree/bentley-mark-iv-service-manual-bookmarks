PYTHON = python3

SRC_DIR = ./src

DEFINITIONS_DIR = ./definitions
BUILD_DIR = ./build
OUT_DIR = .

all: $(OUT_DIR)/bookmarks.txt $(BUILD_DIR)/section_page_numbers.json

$(OUT_DIR)/bookmarks.txt: $(BUILD_DIR)/toc_bookmarks.txt $(BUILD_DIR)/additional_bookmarks.txt $(BUILD_DIR)/index_bookmarks.txt
	cat $^ > $@

# Section page numbers

#.PHONY: $(BUILD_DIR)/section_page_numbers.json

$(BUILD_DIR)/section_page_numbers.json: $(BUILD_DIR)/toc_definitions.json
	$(PYTHON) $(SRC_DIR)/extract_section_page_numbers.py < $? > $@

# Table of contents

$(BUILD_DIR)/toc_bookmarks.txt: $(BUILD_DIR)/toc_definitions.json
	@mkdir -p $(BUILD_DIR)
	$(PYTHON) $(SRC_DIR)/generate_toc_bookmarks.py < $? > $@

$(BUILD_DIR)/toc_definitions.json: $(DEFINITIONS_DIR)/TableOfContents.csv
	$(PYTHON) $(SRC_DIR)/process_toc_definitions.py < $? > $@

# Additional bookmarks
# NOTE: The additional bookmarks csv & json files use the Table of Contents structure

$(BUILD_DIR)/additional_bookmarks.txt : $(BUILD_DIR)/additional_definitions.json
	@mkdir -p $(BUILD_DIR)
	$(PYTHON) $(SRC_DIR)/generate_toc_bookmarks.py < $? > $@

$(BUILD_DIR)/additional_definitions.json: $(DEFINITIONS_DIR)/Additional.csv
	$(PYTHON) $(SRC_DIR)/process_toc_definitions.py < $? > $@

# Index bookmarks

$(BUILD_DIR)/index_bookmarks.txt: $(BUILD_DIR)/index_definitions.json
	$(PYTHON) $(SRC_DIR)/generate_index_bookmarks.py < $? > $@

#.PHONY: $(BUILD_DIR)/index_definitions.json

$(BUILD_DIR)/index_definitions.json: $(DEFINITIONS_DIR)/Index.txt $(BUILD_DIR)/section_page_numbers.json
	$(PYTHON) $(SRC_DIR)/process_index_definitions.py $(BUILD_DIR)/section_page_numbers.json < $< > $@

