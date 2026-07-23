# Field Definition

## JSON Field Definition

- [schema.json](schema.json)

## Address Field Defintion

| Field | Description                 |
| ----: | --------------------------- |
|   `R` | country                     |
|   `1` | ~~address_line_1~~          |
|   `2` | ~~address_line_2~~          |
|   `A` | street_address              |
|   `S` | admin_area                  |
|   `C` | locality                    |
|   `D` | dependent_locality          |
|   `Z` | postal_code                 |
|   `X` | sorting_code                |
|   `N` | recipient                   |
|   `O` | organization                |
|   `T` | landmark_address_descriptor |
|   `F` | landmark_affix              |
|   `L` | landmark_name               |

## Width Overrides

| Field | Description |
| ----: | ----------- |
|   `N` | short       |
|   `S` | short       |
|   `L` | long        |

## References

- <https://github.com/google/libaddressinput/wiki/AddressValidationMetadata>
- <https://github.com/google/libaddressinput/blob/master/common/src/main/java/com/google/i18n/addressinput/common/AddressDataKey.java>
- <https://github.com/google/libaddressinput/blob/master/common/src/main/java/com/google/i18n/addressinput/common/AddressData.java>
- <https://github.com/google/libaddressinput/blob/master/common/src/main/java/com/google/i18n/addressinput/common/AddressField.java>
