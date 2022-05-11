<?php

namespace Tests\Feature;

use Api;
use PHPUnit\Framework\TestCase;

/**
 * Class ApiTest.
 *
 * @covers \Api
 */
class ApiTest extends TestCase
{
    protected $api;

    protected function setUp(): void
    {
        parent::setUp();
        $this->api = new Api();
    }

    protected function tearDown(): void
    {
        parent::tearDown();

        unset($this->api);
    }

    /**
     * We need to have at least one keyword to search tweets
     */
    public function testFailure1()
    {
        $this->assertGreaterThanOrEqual(1, $this->api->$phrases);
    }

    /**
     * We need to have the Helper object created, otherwise we clearly have a problem
     */
    public function testFailure2()
    {
        $this->assertNotNull(1, $this->api->$helper);
    }

    /**
     * We must not allow our Run() function to return false, it means that at some point the api returned an empty object
     */
    public function testFailure3()
    {
        $this->assertTrue($this->api->Run());
    }

    public function testRun(): void
    {
        /** @todo This test is incomplete. */
        $this->markTestIncomplete();
    }
}
