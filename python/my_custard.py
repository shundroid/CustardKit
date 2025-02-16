from source.custard import *

custard = Custard(
    identifier="my_custard",
    language=Language.ja_JP,
    input_style=InputStyle.direct,
    metadata=Metadata(
        custard_version="1.0",
        display_name="私のカスタード",
    ),
    interface=Interface(
        key_style=KeyStyle.tenkey_style,
        key_layout=GridFitLayout(row_count=2, column_count=2),
        keys=[
            KeyData(
                specifier=GridFitSpecifier(x=0, y=0),
                key=SystemKey(SystemKeyType.change_keyboard)
            ),
            KeyData(
                specifier=GridFitSpecifier(x=0, y=1),
                key=CustomKey(
                    design=KeyDesign(
                        label=TextLabel(text="あ"),
                        color=KeyColor.normal
                    ),
                    press_actions=[],
                    longpress_actions=LongpressAction(
                        start=[
                            DeleteAction(1),
                        ]
                    ),
                    variations=[
                        FlickVariationData(
                            direction=FlickDirection.left,
                            key=Variation(
                                design=VariationDesign(
                                    label=TextLabel(text="い"),
                                ),
                                press_actions=[
                                    InputAction("い")
                                ],
                                longpress_actions=LongpressAction()
                            )
                        )
                    ]
                )
            ),

            KeyData(
                specifier=GridFitSpecifier(x=1, y=0),
                key=CustomKey(
                    design=KeyDesign(
                        label=TextLabel(text="あ"),
                        color=KeyColor.normal
                    ),
                    press_actions=[],
                    longpress_actions=LongpressAction(
                        start=[
                            DeleteAction(1),
                        ]
                    ),
                    variations=[
                        FlickVariationData(
                            direction=FlickDirection.left,
                            key=Variation(
                                design=VariationDesign(
                                    label=TextLabel(text="い"),
                                ),
                                press_actions=[
                                    InputAction("い")
                                ],
                            )
                        )
                    ]
                )
            ),

            KeyData(
                specifier=GridFitSpecifier(x=1, y=1),
                key=CustomKey(
                    design=KeyDesign(
                        label=TextLabel(text="あ"),
                        color=KeyColor.normal
                    ),
                    press_actions=[],
                    longpress_actions=LongpressAction(
                        start=[
                            DeleteAction(1),
                        ]
                    ),
                    variations=[
                        FlickVariationData(
                            direction=FlickDirection.left,
                            key=Variation(
                                design=VariationDesign(
                                    label=TextLabel(text="い"),
                                ),
                                press_actions=[
                                    InputAction("い")
                                ],
                            )
                        )
                    ]
                )
            ),
        ]
    )
)

custard.write(to="./results/my_custard.json")
