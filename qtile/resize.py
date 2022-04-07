from libqtile.command import lazy


class Resize:
    @staticmethod
    def RS_UP():
        return (
            lazy.layout.grow_up(),
            lazy.layout.grow(),
            lazy.layout.decrease_nmaster(),
        )

    @staticmethod
    def RS_DOWN():
        return (
            lazy.layout.grow_down(),
            lazy.layout.shrink(),
            lazy.layout.increase_nmaster(),
        )

    @staticmethod
    def RS_LEFT():
        return (
            lazy.layout.grow_left(),
            lazy.layout.shrink(),
            lazy.layout.decrease_ratio(),
            lazy.layout.add(),
        )

    @staticmethod
    def RS_RIGHT():
        return (
            lazy.layout.grow_right(),
            lazy.layout.grow(),
            lazy.layout.increase_ratio(),
            lazy.layout.delete(),
        )
