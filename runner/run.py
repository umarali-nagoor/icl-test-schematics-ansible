import logging

logger = logging.getLogger(__name__)


def run_playbook(playbook, inventory, runner):
    logger.info("Entering run_playbook")
    try:
        result = runner.run(playbook)
    except Exception:
        logger.error("playbook failed id=%s", playbook.id, exc_info=True)
        raise
    logger.info("playbook finished id=%s rc=%s", playbook.id, result.rc)
    logger.info("Exiting run_playbook")
    return result


def poll_playbook_status(runner, timeout: int = 300) -> str:
    """Poll until playbook completes or timeout."""
    import time
    elapsed = 0
    while elapsed < timeout:
        status = runner.get_status()
        logger.info("playbook status poll: %s", status)
        if status.get("rc") is not None:
            logger.info("playbook completed: %s", status)
            return status["rc"]
        time.sleep(5)
        elapsed += 5
    logger.error("playbook timed out after %ds, last status: %s", timeout, status)
    return "timeout"
