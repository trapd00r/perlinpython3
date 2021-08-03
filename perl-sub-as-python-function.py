# Magnus Woldrich, m@japh.se, japh@irc.libera.chat
# 2021-08-03 08:42:41
import perl as japh
import sys

# let's grab some arguments from python
filenames = sys.argv

# create a perl subroutine using perl.eval:
# make sure to omit the return statement
basename_and_colorize = japh.eval("""
  sub {
    use File::Basename;
    use File::LsColor qw(ls_color); # https://github.com/trapd00r/File-LsColor

    my $file = shift;
    ls_color(basename($file));

  }
""")

# use python to iterate over the given argments, and for each argument,
# call the perl subroutine using perl.call(sub, args), and store it in a
# python variable

for f in filenames:
  base = japh.call(basename_and_colorize, f)
  print(base)
