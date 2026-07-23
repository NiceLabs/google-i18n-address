# Field Definition

## JSON Field Definition

- `countries` \
  Identifies the countries for which data is provided.
- `fmt` \
  The standard format string. This identifies which fields can be used in the address, along with their order. This also carries additional information for use in formatting the fields into multiple lines. This is also used to indicate which fields should _NOT_ be used for an address.
- `id` \
  The unique ID of the region, in the form of a path from parent IDs to the key.
- `isoid` \
  The CLDR (Common Locale Data Repository) country code (https://cldr.unicode.org) for this region, if there is one. This value must be present.
- `key` \
  The key of the region, unique to its parent. If there is an accepted abbreviation for this region, then the key will be set to this and name will be set to the local name for this region. If there is no accepted abbreviation, then this key will be the local name and there will be no local name specified. This value must be present.
- `lang` \
  The default language of any data for this region, if known.
- `languages` \
  The languages used by any data for this region, if known.
- `lfmt` \
  The latin format string FMT used when a country defines an alternative format for use with the latin script, such as in China.
- `locality_name_type` \
  Indicates the type of the name used for the locality (city) field.
- `require` \
  Indicates which fields must be present in a valid address.
- `state_name_type` \
  Indicates the type of the name used for the state (administrative area) field.
- `sublocality_name_type` \
  Indicates the type of the name used for the sublocality field.
- `sub_keys` \
  Encodes the KEY value of all the children of this region.
- `sub_lnames` \
  Encodes the transliterated latin name value of all the children of this region, if the local names are not in latin script already.
- `sub_names` \
  Encodes the local name value of all the children of this region.
- `sub_mores` \
  Indicates, for each child of this region, whether that child has additional children.
- `width_overrides` \
  Encodes width overrides for specific fields.
- `xzip` \
  Encodes the ZIP value for the subtree beneath this region.
- `zip` \
  Encodes the postal code pattern if at the country level, and the postal code prefix if at a level below country.
- `zip_name_type` \
  Indicates the type of the name used for the ZIP (postal code) field.
- `postprefix` \
  Common prefix for postal code.
- `posturl` \
  Helper URL for postal code.

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
