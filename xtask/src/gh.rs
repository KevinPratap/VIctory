//! Running git, gh and cargo, and reading what they print, for the Forge and
//! the claims (no JSON crate: gh's `--jq` prints tab-separated fields).

use std::path::Path;
use std::process::Command;

use anyhow::{Context, Result, bail};

/// Output of a command run in `dir`: whether it succeeded, stdout, stderr.
pub struct Out {
    pub ok: bool,
    pub code: Option<i32>,
    pub stdout: String,
    pub stderr: String,
}

pub fn run(program: &str, args: &[&str], dir: &Path) -> Result<Out> {
    let o = Command::new(program)
        .args(args)
        .current_dir(dir)
        .output()
        .with_context(|| format!("running {program}"))?;
    Ok(Out {
        ok: o.status.success(),
        code: o.status.code(),
        stdout: String::from_utf8_lossy(&o.stdout).into_owned(),
        stderr: String::from_utf8_lossy(&o.stderr).into_owned(),
    })
}

/// [`run`], failing unless the command succeeds; returns stdout.
pub fn ok(program: &str, args: &[&str], dir: &Path) -> Result<String> {
    let o = run(program, args, dir)?;
    if !o.ok {
        bail!("{program} {}: {}", args.join(" "), o.stderr.trim());
    }
    Ok(o.stdout)
}

/// The fields of one line jq's `@tsv` printed.
pub fn tsv(line: &str) -> Vec<String> {
    line.split('\t')
        .map(|f| {
            let mut s = String::with_capacity(f.len());
            let mut it = f.chars();
            while let Some(c) = it.next() {
                if c != '\\' {
                    s.push(c);
                    continue;
                }
                match it.next() {
                    Some('t') => s.push('\t'),
                    Some('n') => s.push('\n'),
                    Some('r') => s.push('\r'),
                    Some(o) => s.push(o),
                    None => s.push('\\'),
                }
            }
            s
        })
        .collect()
}

/// Seconds since 1970 of an ISO 8601 UTC time (`2026-11-24T20:02:43Z`).
pub fn unix(iso: &str) -> i64 {
    let n = |r: std::ops::Range<usize>| iso.get(r).and_then(|s| s.parse::<i64>().ok()).unwrap_or(0);
    let (y, m, d) = (n(0..4), n(5..7), n(8..10));
    days_from_civil(y, m, d) * 86_400 + n(11..13) * 3_600 + n(14..16) * 60 + n(17..19)
}

/// Days since 1970-01-01 of a proleptic Gregorian date (Howard Hinnant's
/// algorithm).
fn days_from_civil(y: i64, m: i64, d: i64) -> i64 {
    let y = if m <= 2 { y - 1 } else { y };
    let era = y.div_euclid(400);
    let yoe = y - era * 400;
    let mp = (m + 9) % 12;
    let doy = (153 * mp + 2) / 5 + d - 1;
    let doe = yoe * 365 + yoe / 4 - yoe / 100 + doy;
    era * 146_097 + doe - 719_468
}

/// `YYYY-MM-DD HH:MM` of seconds since 1970 (UTC).
pub fn date(t: i64) -> String {
    let (days, secs) = (t.div_euclid(86_400), t.rem_euclid(86_400));
    let z = days + 719_468;
    let era = z.div_euclid(146_097);
    let doe = z - era * 146_097;
    let yoe = (doe - doe / 1460 + doe / 36_524 - doe / 146_096) / 365;
    let doy = doe - (365 * yoe + yoe / 4 - yoe / 100);
    let mp = (5 * doy + 2) / 153;
    let d = doy - (153 * mp + 2) / 5 + 1;
    let m = if mp < 10 { mp + 3 } else { mp - 9 };
    let y = yoe + era * 400 + i64::from(m <= 2);
    format!(
        "{y:04}-{m:02}-{d:02} {:02}:{:02}",
        secs / 3_600,
        secs % 3_600 / 60
    )
}

pub fn now() -> i64 {
    std::time::SystemTime::now()
        .duration_since(std::time::UNIX_EPOCH)
        .map_or(0, |d| d.as_secs() as i64)
}

/// A Markdown table cell.
pub fn cell(s: &str) -> String {
    s.replace('|', "\\|").replace(['\n', '\r'], " ")
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn tsv_fields_unescape() {
        assert_eq!(
            tsv("12\ta\\tb\tline\\nnext\\\\"),
            ["12", "a\tb", "line\nnext\\"]
        );
    }

    #[test]
    fn dates_round_trip() {
        let t = unix("2026-11-24T20:02:43Z");
        assert_eq!(date(t), "2026-11-24 20:02");
        assert_eq!(unix("1970-01-01T00:00:00Z"), 0);
        assert_eq!(
            unix("2000-03-01T00:00:00Z") - unix("2000-02-28T00:00:00Z"),
            2 * 86_400
        );
    }
}
