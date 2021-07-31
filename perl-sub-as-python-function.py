import perl as japh
import sys

filename = str(sys.argv[0])

basename_and_colorize = japh.eval("""
  sub {
    use File::Basename;
    use File::LsColor qw(ls_color);
    my $name = shift;
    ls_color(basename($name));
  }
""")

base = japh.call(basename_and_colorize, filename)
print(base)
