label screen_displayables:

    e "There are quite a few screen displayables. Here, I'll tell you about some of the most important ones."

label screen_displayables_menu:

    $ reset_example()

    menu:

        e "What would you like to know about?"

        "Properties all displayables share.":
            call screen_displayable_properties

        "Simple displayables.":
            call simple_screen_displayables

        "That's all for now.":
            return

    jump screen_displayables_menu



label screen_displayable_properties:

    e "There are a few properties that every screen language displayable shares. Here, I'll demonstrate them for you."

    example large:
        screen pos_example():
            frame:
                xalign 0.5 ypos 50
                text _("This uses position properties.")

    show screen pos_example
    with dissolve

    e "First off, every screen language displayable supports the position properties. When the container a displayable is in supports it, you can use properties like align, anchor, pos, and so so on."

    example:
        screen at_example():
            frame:
                xalign 0.5 ypos 50
                text _("And the world turned upside down..."):
                    at rotated

        transform rotated:
            rotate 180 rotate_pad False

    hide screen pos_example
    show screen at_example
    with dissolve

    e "The at transform applies a transform to the displayable, the same way the at clause in the show statement does."

    e "The at clause can be used for all sorts of purposes. It can animate and transform the displayable. Here, we're rotating the text upside down."


#     example large:
#         screen event_example():
#             frame:
#                 at inout
#                 xalign 0.5 ypos 50
#                 text _("This is an event.") at textform
#
#
#         transform inout:
#             on show:
#                 zoom 1.5 alpha 0.0
#                 linear .5 zoom 1.0 alpha 1.0
#
#             on hide:
#                 linear .5 zoom 1.5 alpha 0.0

#
#     example:
#         screen default_example():
#             frame:
#                 xalign 0.5 ypos 50
#
#                 vbox:
#
#                     textbutton "Choice 1" action Return(1)
#                     textbutton "Choice 2" action Return(1) default True
#                     textbutton "Choice 3" action Return(1)


    hide screen at_example
    with dissolve

    show example say_screen

    e "The id property is mostly used with the say screen, which is used to show dialogue. Outside of the say screen, it isn't used much."

    e "It tells Ren'Py which displayables are the background window, 'who' is speaking, and 'what' is being said. This used to apply per-Character styles, and help with auto-forward mode."

    example:
        screen style_example():
            frame:
                xalign 0.5 ypos 50
                vbox:
                    text _("Flight pressure in tanks.") style "green_text"
                    text _("On internal power.")
                    text _("Launch enabled.")
                    text _("Liftoff!")

    style green_text:
        color "#c8ffc8"

    show screen style_example
    with dissolve

    e "The style property lets you specify the style of a single displayable."

    example:
        screen style_prefix_example():
            frame:
                xalign 0.5 ypos 50
                vbox:
                    vbox:
                        style_prefix "green"
                        text _("Flight pressure in tanks.")
                        text _("On internal power.")

                    vbox:
                        style_prefix "yellow"
                        text _("Launch enabled.")
                        text _("Liftoff!")

    style yellow_text:
        color "#ffffc8"


    hide screen style_example
    show screen style_prefix_example

    e "The style_prefix property sets the prefix of the style that's used for a displayable and its children."

    e "For example, when the style_prefix property is 'green', the vbox has the 'green_vbox' style, and the text in it has the 'green_text' style."

    hide screen style_prefix_example
    hide example
    with dissolve

    e "There are a few more properties than these, and you can find the rest in the documentation. But these are the ones you can expect to see in your game, in the default screens."

    return

