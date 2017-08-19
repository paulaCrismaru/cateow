VALID_KITTY_TEMPLATE = """
{balloon}
  (.   \   {way}
    \  |    {way}
     \ |___(\--/)
   __/    (  . . )
  "'._.    '-.O.'
       '-.  \ "|\
          '.,,/'.,,
"""
INVALID_KITTY_TEMPLATE = """
{balloon_wrong}
  (.   \   {way}
    \  |    {way}
     \ |___(\--/)
   __/    (  . . )
  "'._.    '-.O.'
       '-.  \ "|\
          '.,,/'.,,
"""

TEXT_1_LINE = "Lorem ipsum dolor sit amet."
TEXT_2_LINES = "Lorem ipsum dolor sit amet, consectetur adipiscing elit."
TEXT_MORE_LINES = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. " \
                  "Sed pellentesque libero eu placerat consequat."

EXPECTED_TEXT_1_LINE = [TEXT_1_LINE]
EXPECTED_TEXT_2_LINES = ["Lorem ipsum dolor sit amet,",
                         "consectetur adipiscing elit."]

EXPECTED_TEXT_MORE_LINES = ["Lorem ipsum dolor sit amet,",
                            "consectetur adipiscing elit. Sed",
                            "pellentesque libero eu placerat",
                            "consequat."]

# pylint: disable=trailing-whitespace
ONE_LINE_BALLOON = \
"""  ___________________________  
< Lorem ipsum dolor sit amet. >
  ---------------------------  """

TWO_LINE_BALLOON = \
"""  ____________________________  
/ Lorem ipsum dolor sit amet,  \\
\\ consectetur adipiscing elit. /
  ----------------------------  """

MULTI_LINE_BALLOON = \
"""  ________________________________  
/ Lorem ipsum dolor sit amet,      \\
| consectetur adipiscing elit. Sed |
| pellentesque libero eu placerat  |
\\ consequat.                       /
  --------------------------------  """
