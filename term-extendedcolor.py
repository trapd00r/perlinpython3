# Magnus Woldrich, m@japh.se, japh@irc.libera.chat
# 2021-08-04 09:18:39
# Exporting functions from Term::ExtendedColor into python
import perl as japh
import sys

# let's grab some arguments from python
filenames = sys.argv


fg = japh.eval("""
  sub {
    use Term::ExtendedColor qw(fg);
    my($color, $text) = @_;
    fg($color, $text);
  }
""")

bg = japh.eval("""
  sub {
    use Term::ExtendedColor qw(bg);
    my($color, $text) = @_;
    bg($color, $text);
  }
""")

bold = japh.eval("""
  sub {
    use Term::ExtendedColor qw(bold);
    my $text = shift;
    bold($text);
  }
""")
italic = japh.eval("""
  sub {
    use Term::ExtendedColor qw(italic);
    my $text = shift;
    italic($text);
  }
""")

bolditalic = japh.eval("""
  sub {
    use Term::ExtendedColor qw(bold italic);
    my $text = shift;
    bold(italic($text));
  }
""")

underline = japh.eval("""
  sub {
    use Term::ExtendedColor qw(underline);
    my $text = shift;
    underline($text);
  }
""")

inverse = japh.eval("""
  sub {
    use Term::ExtendedColor qw(inverse);
    my $text = shift;
    inverse($text);
  }
""")


for f in filenames:
  f += ' '
  print(  fg(196, f)
        + bg(88, f)
        + bold(f)
        + italic(f)
        + bolditalic(f)
        + underline(f)
        + inverse(f)
      )

print(fg(88, bg(196, bold(italic(underline(inverse('All together now!')))))))

