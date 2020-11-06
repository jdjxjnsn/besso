import asyncio
import sys
import io
import traceback


async def aexec(code, message, replied=None):

    exec(
        f"from utilities import utilities as u\nasync def __ex(message,replied):\n global u"
        + "".join(f"\n {l}" for l in code.split("\n"))
    )

    return await locals()["__ex"](message, replied)


async def run(msg, matches, chat_id, step, crons=None):
    if not (msg.out):
        message = await msg.reply("Please, wait...")
    else:
        message = msg
    old_stderr = sys.stderr
    old_stdout = sys.stdout
    redirected_output = sys.stdout = io.StringIO()
    redirected_error = sys.stderr = io.StringIO()
    stdout, stderr, exc = None, None, None
    if msg.is_reply and matches == "exec":
        msg = await msg.get_reply_message()
        if msg.raw_text:
            cmd = msg.raw_text
        else:
            cmd = "print('Please, reply to text message.')"
    elif matches[0] == "exec":
        cmd = matches[1]
    else:
        return [message.delete()]
    try:
        await aexec(cmd, message, msg)
    except Exception:
        exc = traceback.format_exc()

    stdout = redirected_output.getvalue()
    stderr = redirected_error.getvalue()
    sys.stdout = old_stdout
    sys.stderr = old_stderr

    evaluation = ""
    if exc:
        evaluation = exc
    elif stderr:
        evaluation = stderr
    elif stdout:
        evaluation = stdout
    else:
        evaluation = "Success"

    final_output = "**EVAL**: `{}` \n\n **OUTPUT**: \n`{}` \n".format(cmd, evaluation)
    if len(final_output) > 4000:
            with io.BytesIO(str.encode(final_output)) as out_file:
                out_file.name = "exec.text"
                await message.reply(file=out_file)
            await message.delete()
    else:
            await message.edit(final_output)


    return []


plugin = {
    "name": "",
    "desc": " — — — — — — — — —.",
    "usage": ["❏︙/exec <امر معرفه خطاء الملف + اسم الملف>"],
    "run": run,
    "sudo": True,
    "patterns": ["^[!/#](exec) (.+)$", "^[!/#](exec)$"],
}
