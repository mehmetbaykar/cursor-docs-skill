---
title: "Manage Grok Bot computers"
source: https://cursor.com/docs/grok-bot/computers
path: /docs/grok-bot/computers
---

# Manage Grok Bot computers

Each member of your team gets one hosted computer where every Bot they run does its work. **Grok Bot Computers** on the [Grok Bot page of the Cursor dashboard](https://cursor.com/dashboard/bot) lets an organization admin recreate or terminate those computers for many members at once, with a confirmation step and a result for each member. For the rest of the admin controls, see [Grok Bot for Teams and Enterprise](https://cursor.com/docs/grok-bot/teams.md).

**Grok Bot Computers is Enterprise only**, and it appears only for
organization admins. Team admin rights aren't enough, because one computer
spans every team the member belongs to. Members never see this control.

## Recreate or terminate

Both actions keep the member's durable disk. They differ in what happens next.

| Action        | What happens                                                                                                                                                                                                                     | What members keep                                                                                                                                                                                                     | When to use it                                                                                                                                                            |
| ------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Recreate**  | Builds a replacement computer on the latest image and runs [Team Setup](https://cursor.com/docs/grok-bot/private-networks.md). The current computer stays available until the replacement is ready, then Grok Bot switches over. | Synced Bots, files, and logins. A Bot that is mid-turn is asked to pause at a safe point and resumes on the new computer. If it can't pause in time, the recreate for that member is not started and shows as failed. | Roll out a new image, a changed [network policy](https://cursor.com/docs/grok-bot/security.md#network-policy), or an updated Team Setup manifest to many members at once. |
| **Terminate** | Deletes the member's computer, running or hibernated. It does not restart on its own; the member's next session starts a fresh computer on the same durable disk.                                                                | Synced Bots, files, and logins. Running work stops.                                                                                                                                                                   | End a member's current work, or clear a computer that is stuck. Terminating does not remove access; see the [FAQ](https://cursor.com/docs/grok-bot/computers.md#faq).     |

Both actions remove apps and packages that members installed themselves. Anything your Team Setup manifests install comes back on the new computer.

## Run an operation

### Open Grok Bot Computers

Go to [Grok Bot in the Cursor dashboard](https://cursor.com/dashboard/bot),
find **Grok Bot Computers**, and select **Manage**.

### Select members

Search by name or email, then check the members you want. **Select all**
picks everyone in the current results.

### Choose an action

Select **Recreate VMs…** or **Terminate VMs…**. A confirmation screen
restates the action and the number of members it affects.

### Confirm

Select **Recreate VMs** or **Terminate VMs** to start. Members without a
computer are skipped.

### Watch the results

A progress card shows queued, running, complete, skipped, and failed
counts, and each member's row shows its status. When the operation
finishes, select **Done** to clear the results and start another.

## How an operation runs

- **It runs on Cursor's side.** Closing the dialog or the browser doesn't stop it. Reopen **Manage** in the same browser to pick the progress back up.
- **Large operations take a while.** Members are processed in batches, and each recreate waits for the replacement computer to be ready before it counts as complete.
- **One operation per team at a time.** The action buttons stay disabled until you select **Done** on the finished results.
- **Retry Start never duplicates work.** Use it when the dashboard can't confirm the operation started.

## Skipped and failed members

A finished operation lists a result for every member you selected.

| Result                                        | Meaning                                                                                                                                                                          | What to do                                                                                                                                                                                                                       |
| --------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Skipped**, No VM                            | The member had no running or hibernated computer.                                                                                                                                | Nothing.                                                                                                                                                                                                                         |
| **Skipped**, Action could not be completed    | The member left the team, or their account changed, while the operation was queued.                                                                                              | Nothing.                                                                                                                                                                                                                         |
| **Failed**, Another recreation is in progress | The member's computer is already being recreated, by an update or another admin.                                                                                                 | Wait for it to finish, then run again for this member.                                                                                                                                                                           |
| **Failed**, VM scan incomplete                | Cursor couldn't confirm the state of the member's computer, so it made no change.                                                                                                | Run the operation again in a few minutes.                                                                                                                                                                                        |
| **Failed**, Action could not be completed     | The recreate or terminate did not finish. For a recreate, a Bot on the member's computer may have been unable to pause in time; the member's current computer is left as it was. | Run the operation again for the affected members, once their Bots are idle if you can. If it fails twice, [contact support](https://cursor.com/help/grok-bot/get-help.md) with the member's email and the time of the operation. |

## What members see

During a recreate, the desktop app shows **Updating Grok Bot's Computer** until the switch completes. Bots that were working pause at a safe point and continue on the new computer. If a Bot can't pause in time, the member keeps their current computer and that member's result shows as failed. Sign-in sessions inside the computer can drop when it is recreated, so members sign in to company tools again under your identity provider's policies.

After a terminate, the member's next message starts a fresh computer on their durable disk. The reconnect can take a few minutes. Bots, files, and logins that had synced come back; a turn that was running is lost.

## FAQ

### Can I recreate a member's computer from a different team?

Yes. Select the member from any team they belong to. One computer serves
every team the member is in, so recreating or terminating it from one team
affects the same computer everywhere.

### Does terminating stop a member from using Grok Bot?

No. Terminating a computer ends the member's current work; their next
message starts a fresh computer on the same durable disk, with their Bots,
files, and logins. To remove access, remove the member from the team or turn
off their access with **Manage Group Access**, and revoke their sessions in
your identity provider. See
[Enable Grok Bot](https://cursor.com/docs/grok-bot/teams.md#enable-grok-bot).

## Related pages

- [Grok Bot for Teams and Enterprise](https://cursor.com/docs/grok-bot/teams.md)
- [Grok Bot security](https://cursor.com/docs/grok-bot/security.md)
- [Connect to private networks](https://cursor.com/docs/grok-bot/private-networks.md)
- [Grok Bot computer](https://cursor.com/help/grok-bot/computer-recovery.md)
